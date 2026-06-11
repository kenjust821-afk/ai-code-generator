from fastapi import APIRouter, HTTPException
from app.schemas.conversation import ConversationCreate, ConversationResponse, MessageCreate
from app.services.conversation_service import ConversationService
from typing import List
import logging

router = APIRouter()
logger = logging.getLogger(__name__)
conv_service = ConversationService()


@router.get("", response_model=List[ConversationResponse])
async def get_conversations():
    """Get all conversations"""
    try:
        conversations = await conv_service.get_all_conversations()
        return conversations
    except Exception as e:
        logger.error(f"Error fetching conversations: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("", response_model=ConversationResponse)
async def create_conversation(request: ConversationCreate):
    """Create new conversation"""
    try:
        conversation = await conv_service.create_conversation(
            title=request.title,
            description=request.description,
            language=request.language,
            ai_model=request.ai_model
        )
        return conversation
    except Exception as e:
        logger.error(f"Error creating conversation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{conversation_id}", response_model=ConversationResponse)
async def get_conversation(conversation_id: int):
    """Get conversation details"""
    try:
        conversation = await conv_service.get_conversation(conversation_id)
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
        return conversation
    except Exception as e:
        logger.error(f"Error fetching conversation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/{conversation_id}/messages")
async def add_message(conversation_id: int, request: MessageCreate):
    """Add message to conversation"""
    try:
        message = await conv_service.add_message(
            conversation_id=conversation_id,
            content=request.content,
            role=request.role,
            message_type=request.message_type
        )
        return message
    except Exception as e:
        logger.error(f"Error adding message: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
