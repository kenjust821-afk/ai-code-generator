import React, { useState } from 'react';
import { Download, FileJson, Package } from 'lucide-react';
import '../styles/FileDownload.css';

interface FileDownloadProps {
  code: string;
  language: string;
}

const FileDownload: React.FC<FileDownloadProps> = ({ code, language }) => {
  const [isDownloading, setIsDownloading] = useState(false);

  const getFileExtension = (lang: string): string => {
    const extensions: Record<string, string> = {
      python: '.py',
      javascript: '.js',
      typescript: '.ts',
      java: '.java',
      cpp: '.cpp',
      csharp: '.cs',
      go: '.go',
      rust: '.rs',
      php: '.php',
      ruby: '.rb',
    };
    return extensions[lang.toLowerCase()] || '.txt';
  };

  const downloadFile = async (format: 'raw' | 'zip' | 'pdf') => {
    if (!code) return;

    setIsDownloading(true);
    try {
      const filename = `generated_code${getFileExtension(language)}`;
      const element = document.createElement('a');
      const file = new Blob([code], { type: 'text/plain' });
      element.href = URL.createObjectURL(file);
      element.download = filename;
      document.body.appendChild(element);
      element.click();
      document.body.removeChild(element);
    } catch (error) {
      console.error('Download error:', error);
    } finally {
      setIsDownloading(false);
    }
  };

  if (!code) {
    return null;
  }

  return (
    <div className="file-download">
      <button
        onClick={() => downloadFile('raw')}
        disabled={isDownloading}
        className="download-btn raw"
      >
        <Download size={18} /> Download File
      </button>
      <button
        onClick={() => downloadFile('zip')}
        disabled={isDownloading}
        className="download-btn zip"
      >
        <Package size={18} /> Download ZIP
      </button>
      <button
        onClick={() => downloadFile('pdf')}
        disabled={isDownloading}
        className="download-btn pdf"
      >
        <FileJson size={18} /> Download PDF
      </button>
    </div>
  );
};

export default FileDownload;
