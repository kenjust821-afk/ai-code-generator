import React, { useState } from 'react';
import { Send, Loader } from 'lucide-react';
import '../styles/ChatInterface.css';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  code?: string;
  language?: string;
  timestamp: Date;
}

interface ChatInterfaceProps {
  messages: Message[];
  onSendMessage: (message: string) => void;
  isLoading: boolean;
  chatEndRef: React.RefObject<HTMLDivElement>;
}

const ChatInterface: React.FC<ChatInterfaceProps> = ({
  messages,
  onSendMessage,
  isLoading,
  chatEndRef,
}) => {
  const [inputValue, setInputValue] = useState('');

  const handleSend = () => {
    if (inputValue.trim()) {
      onSendMessage(inputValue);
      setInputValue('');
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="chat-interface">
      <div className="messages-container">
        {messages.length === 0 ? (
          <div className="empty-state">
            <div className="empty-icon">💬</div>
            <h2>Start a conversation</h2>
            <p>Ask me to generate code for any purpose</p>
          </div>
        ) : (
          messages.map((message) => (
            <div
              key={message.id}
              className={`message message-${message.role}`}
            >
              <div className="message-avatar">
                {message.role === 'user' ? '👤' : '🤖'}
              </div>
              <div className="message-content">
                <p>{message.content}</p>
                {message.code && (
                  <div className="message-code-preview">
                    <code>{message.code.substring(0, 200)}...</code>
                  </div>
                )}
              </div>
            </div>
          ))
        )}
        {isLoading && (
          <div className="message message-assistant">
            <div className="message-avatar">🤖</div>
            <div className="message-content">
              <div className="loading-dots">
                <Loader className="spinner" />
                <p>Generating code...</p>
              </div>
            </div>
          </div>
        )}
        <div ref={chatEndRef} />
      </div>

      <div className="input-area">
        <textarea
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Describe the code you want to generate..."
          className="message-input"
          disabled={isLoading}
        />
        <button
          onClick={handleSend}
          disabled={isLoading || !inputValue.trim()}
          className="send-button"
        >
          <Send size={20} />
        </button>
      </div>
    </div>
  );
};

export default ChatInterface;
