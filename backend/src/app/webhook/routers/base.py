import json
import logging
from contextlib import suppress

import sqlalchemy.exc
from aiogram.utils.markdown import hbold, hcode
from fastapi import APIRouter, Depends, HTTPException
from starlette.requests import Request

from app.infrastructure.database.repo.requests import RequestsRepo
from app.webhook.utils import get_repo
from app.webhook.auth import TelegramUser, get_twa_user

router = APIRouter()

@router.get("/questions")
async def get_questions(request: Request, repo: RequestsRepo = Depends(get_repo), user: TelegramUser = Depends(get_twa_user)):
    print(f"User: {user}")
    print(f"User id: {user.id}, username: {user.username}, first_name: {user.first_name}, last_name: {user.last_name}, language_code: {user.language_code}, allows_write_to_pm: {user.allows_write_to_pm}, photo_url: {user.photo_url}")
    questions = [
        {
            "question_id": 1,
            "question_text": "Who is the best at coding?",
            "answers": [
                {"user_id": 1, "user_name": "Alice", "answer_text": "Alice"},
                {"user_id": 2, "user_name": "Bob", "answer_text": "Bob"},
                {"user_id": 3, "user_name": "Charlie", "answer_text": "Charlie"},
                {"user_id": 4, "user_name": "Diana", "answer_text": "Diana"},
            ]
        },
        {
            "question_id": 2,
            "question_text": "Who is the most helpful?",
            "answers": [
                {"user_id": 5, "user_name": "Eve", "answer_text": "Eve"},
                {"user_id": 6, "user_name": "Frank", "answer_text": "Frank"},
                {"user_id": 7, "user_name": "Grace", "answer_text": "Grace"},
                {"user_id": 8, "user_name": "Heidi", "answer_text": "Heidi"},
            ]
        },
        {
            "question_id": 3,
            "question_text": "Who has the best jokes?",
            "answers": [
                {"user_id": 9, "user_name": "Ivan", "answer_text": "Ivan"},
                {"user_id": 10, "user_name": "Judy", "answer_text": "Judy"},
                {"user_id": 11, "user_name": "Ken", "answer_text": "Ken"},
                {"user_id": 12, "user_name": "Laura", "answer_text": "Laura"},
            ]
        },
        {
            "question_id": 4,
            "question_text": "Who is the most creative?",
            "answers": [
                {"user_id": 13, "user_name": "Mallory", "answer_text": "Mallory"},
                {"user_id": 14, "user_name": "Nina", "answer_text": "Nina"},
                {"user_id": 15, "user_name": "Oscar", "answer_text": "Oscar"},
                {"user_id": 16, "user_name": "Peggy", "answer_text": "Peggy"},
            ]
        },
        {
            "question_id": 5,
            "question_text": "Who is the most likely to succeed?",
            "answers": [
                {"user_id": 17, "user_name": "Quentin", "answer_text": "Quentin"},
                {"user_id": 18, "user_name": "Rachel", "answer_text": "Rachel"},
                {"user_id": 19, "user_name": "Steve", "answer_text": "Steve"},
                {"user_id": 20, "user_name": "Trent", "answer_text": "Trent"},
            ]
        }
    ]
    
    return questions
