import React from 'react';
import '../styles/Selector.css';

interface ModelSelectorProps {
  selectedModel: string;
  onModelChange: (model: string) => void;
}

const MODELS = [
  { id: 'openai', name: 'OpenAI GPT-4' },
  { id: 'anthropic', name: 'Anthropic Claude' },
  { id: 'google', name: 'Google Gemini' },
  { id: 'huggingface', name: 'HuggingFace' },
  { id: 'cohere', name: 'Cohere' },
];

const ModelSelector: React.FC<ModelSelectorProps> = ({
  selectedModel,
  onModelChange,
}) => {
  return (
    <div className="selector-container">
      <label htmlFor="model-select">AI Model</label>
      <select
        id="model-select"
        value={selectedModel}
        onChange={(e) => onModelChange(e.target.value)}
        className="selector"
      >
        {MODELS.map((model) => (
          <option key={model.id} value={model.id}>
            {model.name}
          </option>
        ))}
      </select>
    </div>
  );
};

export default ModelSelector;
