<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { Placeholder, Section, Sections } from '@/presentation/components';
  import type { components } from '@/types/schema';
  import { useInviterStore } from '@/store/inviter';

  const router = useRouter();

  const isLoading = ref(true);
  const error = ref<string | null>(null);
  const inviter = ref<components['schemas']['StartData']['inviter'] | null>(null);

  const inviterStore = useInviterStore();

  onMounted(async () => {
    try {
      isLoading.value = true;
      inviter.value = inviterStore.getInviter;

      if (!inviter.value) {
        router.replace({ name: 'onboarding' });
        return;
      }
    } catch (e) {
      error.value = 'Failed to load inviter information. Please try again later.';
      console.error('Error loading inviter:', e);
    } finally {
      isLoading.value = false;
    }
  });

  const continueToApp = () => {
    inviterStore.processInvite();
    router.push({ name: 'questions' });
  };
</script>

<template>
  <div class="inviter-page">
    <div
      v-if="isLoading"
      class="loading"
    >
      Loading...
    </div>
    <div
      v-else-if="error"
      class="error"
    >
      {{ error }}
    </div>
    <Sections v-else>
      <Section standalone>
        <Placeholder
          title="You've Been Invited!"
          caption="Someone wants you to join them on Glow App"
        >
          <template #picture>
            <div class="inviter-icon">✨</div>
          </template>
        </Placeholder>
      </Section>
      <Section padded>
        <div class="inviter-content">
          <Placeholder
            compact
            :title="`${inviter?.title} invited you`"
            :caption="inviter?.group_id ? `Group ID: ${inviter.group_id}` : ''"
          />
          <div
            class="continue-button"
            @click="continueToApp"
          >
            Continue to Glow App
          </div>
        </div>
      </Section>
    </Sections>
  </div>
</template>

<style scoped>
  .inviter-page {
    display: flex;
    flex-direction: column;
    min-height: 100%;
  }

  .inviter-icon {
    font-size: 48px;
    width: var(--size-avatar-big);
    height: var(--size-avatar-big);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .inviter-content {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-10);
  }

  .continue-button {
    padding: var(--spacing-10);
    background-color: var(--color-primary);
    border-radius: var(--size-border-radius-medium);
    color: white;
    text-align: center;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .continue-button:hover {
    opacity: 0.9;
  }

  .loading,
  .error {
    padding: var(--spacing-10);
    text-align: center;
  }

  .error {
    color: var(--color-error);
  }
</style>
