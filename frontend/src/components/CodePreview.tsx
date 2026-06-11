import React, { useEffect, useState } from 'react';
import { AlertCircle, CheckCircle } from 'lucide-react';
import '../styles/CodePreview.css';

interface CodePreviewProps {
  code: string;
  language: string;
}

const CodePreview: React.FC<CodePreviewProps> = ({ code, language }) => {
  const [isValid, setIsValid] = useState<boolean | null>(null);
  const [validationMessage, setValidationMessage] = useState('');

  useEffect(() => {
    if (!code) {
      setIsValid(null);
      return;
    }

    validateCode();
  }, [code, language]);

  const validateCode = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/code/validate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          code,
          language,
        }),
      });

      const data = await response.json();
      setIsValid(data.valid);
      setValidationMessage(
        data.valid ? '✓ Syntax is valid' : '✗ Syntax error detected'
      );
    } catch (error) {
      console.error('Validation error:', error);
      setIsValid(null);
    }
  };

  if (!code) {
    return null;
  }

  return (
    <div className="code-preview">
      <div className="preview-header">
        <h3>Code Validation</h3>
        <div className={`validation-status ${isValid ? 'valid' : 'invalid'}`}>
          {isValid !== null && (
            <>
              {isValid ? (
                <CheckCircle size={20} className="icon valid" />
              ) : (
                <AlertCircle size={20} className="icon invalid" />
              )}
              <span>{validationMessage}</span>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default CodePreview;
