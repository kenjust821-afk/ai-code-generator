import React, { useState, useRef, useEffect } from 'react';
import ChatInterface from './components/ChatInterface';
import CodeEditor from './components/CodeEditor';
import CodePreview from './components/CodePreview';
import LanguageSelector from './components/LanguageSelector';
import ModelSelector from './components/ModelSelector';
import FileDownload from './components/FileDownload';
import './styles/App.css';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  code?: string;
  language?: string;
  timestamp: Date;
}

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [selectedLanguage, setSelectedLanguage] = useState('python');
  const [selectedModel, setSelectedModel] = useState('openai');
  const [isLoading, setIsLoading] = useState(false);
  const [generatedCode, setGeneratedCode] = useState('');
  const chatEndRef = useRef<HTMLDivElement>(null);
  const [conversationId, setConversationId] = useState<number | null>(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSendMessage = async (userMessage: string) => {
    const newUserMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: userMessage,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, newUserMessage]);
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/api/code/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          prompt: userMessage,
          language: selectedLanguage,
          ai_model: selectedModel,
          conversation_id: conversationId,
          temperature: 0.7,
          max_tokens: 2048,
        }),
      });

      if (!response.ok) {
        throw new Error(`API error: ${response.statusText}`);
      }

      const data = await response.json();

      setGeneratedCode(data.generated_code);
      setConversationId(data.conversation_id);

      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: `Generated ${selectedLanguage} code successfully!`,
        code: data.generated_code,
        language: selectedLanguage,
        timestamp: new Date(),
      };

      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Error generating code:', error);
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: `Error: ${error instanceof Error ? error.message : 'Unknown error'}`,
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>🤖 AI Code Generator</h1>
        <p>Generate code for 50+ languages with AI</p>
      </header>

      <div className="app-content">
        <div className="control-panel">
          <LanguageSelector
            selectedLanguage={selectedLanguage}
            onLanguageChange={setSelectedLanguage}
          />
          <ModelSelector
            selectedModel={selectedModel}
            onModelChange={setSelectedModel}
          />
        </div>

        <div className="main-grid">
          <div className="chat-section">
            <ChatInterface
              messages={messages}
              onSendMessage={handleSendMessage}
              isLoading={isLoading}
              chatEndRef={chatEndRef}
            />
          </div>

          <div className="editor-section">
            <div className="editor-tabs">
              <div className="tab active">Generated Code</div>
            </div>
            <CodeEditor code={generatedCode} language={selectedLanguage} />
            <FileDownload code={generatedCode} language={selectedLanguage} />
          </div>
        </div>

        <CodePreview code={generatedCode} language={selectedLanguage} />
      </div>
    </div>
  );
}

export default App;
