export default interface User {
  user_id: number;
  first_name: string;
  last_name: string | null;
  username: string | null;
  is_bot: boolean | null;
  language_code: string | null;
  is_premium: boolean | null;
  added_to_attachment_menu: boolean | null;
  allows_write_to_pm: boolean | null;
  photo_url: string | null;
}
