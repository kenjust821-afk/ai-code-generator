import React, { useState } from 'react';
import { FileVideo, Music, Image, Zap } from 'lucide-react';
import '../styles/MediaCodeGenerator.css';

interface MediaGenerationRequest {
  mediaType: 'image' | 'video' | 'audio' | 'animation';
  description: string;
  codeLanguage: string;
  libraryPreference?: string;
}

const MediaCodeGenerator: React.FC<{
  onGenerate: (request: MediaGenerationRequest) => void;
  isLoading: boolean;
}> = ({ onGenerate, isLoading }) => {
  const [mediaType, setMediaType] = useState<'image' | 'video' | 'audio' | 'animation'>('image');
  const [description, setDescription] = useState('');
  const [codeLanguage, setCodeLanguage] = useState('python');
  const [libraryPreference, setLibraryPreference] = useState('');

  const handleGenerate = () => {
    if (!description.trim()) return;
    
    onGenerate({
      mediaType,
      description,
      codeLanguage,
      libraryPreference: libraryPreference || undefined,
    });
  };

  const mediaOptions = [
    { value: 'image', label: 'Image Generation', icon: Image },
    { value: 'video', label: 'Video Generation', icon: FileVideo },
    { value: 'audio', label: 'Audio Generation', icon: Music },
    { value: 'animation', label: 'Animation', icon: Zap },
  ];

  const languageOptions = {
    image: ['python', 'javascript', 'typescript'],
    video: ['python', 'javascript', 'c++'],
    audio: ['python', 'javascript', 'typescript'],
    animation: ['javascript', 'typescript', 'python'],
  };

  const libraryOptions = {
    image: ['Pillow', 'OpenCV', 'ImageMagick', 'Canvas'],
    video: ['FFmpeg', 'OpenCV', 'MoviePy', 'FFMPEG.wasm'],
    audio: ['Librosa', 'Pydub', 'ToneJS', 'Web Audio API'],
    animation: ['Three.js', 'Babylon.js', 'Canvas API', 'SVG.js'],
  };

  return (
    <div className="media-code-generator">
      <div className="media-header">
        <h3>🎬 Media Code Generator</h3>
        <p>Generate code to create images, videos, audio, and animations</p>
      </div>

      <div className="media-options">
        {mediaOptions.map(({ value, label, icon: Icon }) => (
          <button
            key={value}
            className={`media-option ${mediaType === value ? 'active' : ''}`}
            onClick={() => setMediaType(value as any)}
            disabled={isLoading}
          >
            <Icon size={24} />
            <span>{label}</span>
          </button>
        ))}
      </div>

      <div className="media-form">
        <div className="form-group">
          <label>Describe what you want to create:</label>
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder={`Describe the ${mediaType} you want to generate...`}
            disabled={isLoading}
            rows={4}
          />
        </div>

        <div className="form-row">
          <div className="form-group">
            <label>Programming Language:</label>
            <select
              value={codeLanguage}
              onChange={(e) => setCodeLanguage(e.target.value)}
              disabled={isLoading}
            >
              {languageOptions[mediaType].map((lang) => (
                <option key={lang} value={lang}>
                  {lang.charAt(0).toUpperCase() + lang.slice(1)}
                </option>
              ))}
            </select>
          </div>

          <div className="form-group">
            <label>Library Preference:</label>
            <select
              value={libraryPreference}
              onChange={(e) => setLibraryPreference(e.target.value)}
              disabled={isLoading}
            >
              <option value="">Auto-select best</option>
              {libraryOptions[mediaType].map((lib) => (
                <option key={lib} value={lib}>
                  {lib}
                </option>
              ))}
            </select>
          </div>
        </div>

        <button
          className="generate-button"
          onClick={handleGenerate}
          disabled={!description.trim() || isLoading}
        >
          {isLoading ? 'Generating...' : 'Generate Code'}
        </button>
      </div>
    </div>
  );
};

export default MediaCodeGenerator;
