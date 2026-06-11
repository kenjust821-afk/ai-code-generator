import React from 'react';
import '../styles/Selector.css';

interface LanguageSelectorProps {
  selectedLanguage: string;
  onLanguageChange: (language: string) => void;
}

const LANGUAGES = [
  'python',
  'javascript',
  'typescript',
  'java',
  'cpp',
  'csharp',
  'go',
  'rust',
  'php',
  'ruby',
  'kotlin',
  'swift',
  'scala',
  'haskell',
  'clojure',
  'elixir',
  'erlang',
  'lua',
  'r',
  'matlab',
  'perl',
  'bash',
  'shell',
  'powershell',
  'sql',
  'html',
  'css',
  'scss',
  'less',
  'xml',
  'json',
  'yaml',
  'markdown',
  'dockerfile',
  'terraform',
  'graphql',
  'protobuf',
  'thrift',
  'avro',
  'groovy',
  'dart',
  'lua',
  'vb',
  'cobol',
  'fortran',
  'lisp',
  'scheme',
  'racket',
  'julia',
  'ocaml',
];

const LanguageSelector: React.FC<LanguageSelectorProps> = ({
  selectedLanguage,
  onLanguageChange,
}) => {
  return (
    <div className="selector-container">
      <label htmlFor="language-select">Programming Language</label>
      <select
        id="language-select"
        value={selectedLanguage}
        onChange={(e) => onLanguageChange(e.target.value)}
        className="selector"
      >
        {LANGUAGES.map((lang) => (
          <option key={lang} value={lang}>
            {lang.charAt(0).toUpperCase() + lang.slice(1)}
          </option>
        ))}
      </select>
    </div>
  );
};

export default LanguageSelector;
