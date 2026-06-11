import io
import zipfile
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class FileService:
    def prepare_download(self, code: str, language: str, format: str, filename: str) -> dict:
        """Prepare file for download"""
        try:
            if format == "raw":
                return {"content": code, "format": "raw", "filename": filename}
            elif format == "zip":
                return self._create_zip(code, language, filename)
            elif format == "pdf":
                return self._create_pdf(code, language, filename)
            else:
                raise ValueError(f"Unsupported format: {format}")
        except Exception as e:
            logger.error(f"File preparation failed: {str(e)}")
            raise
    
    def _create_zip(self, code: str, language: str, filename: str) -> dict:
        """Create ZIP file with code"""
        try:
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                ext = self._get_extension(language)
                zip_file.writestr(f"{filename}{ext}", code)
            
            return {
                "content": zip_buffer.getvalue(),
                "format": "zip",
                "filename": f"{filename}.zip",
                "mime_type": "application/zip"
            }
        except Exception as e:
            logger.error(f"ZIP creation failed: {str(e)}")
            raise
    
    def _create_pdf(self, code: str, language: str, filename: str) -> dict:
        """Create PDF file with code"""
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.pdfgen import canvas
            
            pdf_buffer = io.BytesIO()
            c = canvas.Canvas(pdf_buffer, pagesize=letter)
            
            # Add title
            c.setFont("Helvetica-Bold", 16)
            c.drawString(50, 750, f"Generated Code: {filename}")
            
            # Add language info
            c.setFont("Helvetica", 10)
            c.drawString(50, 730, f"Language: {language}")
            
            # Add code (simplified - would need better formatting for production)
            c.setFont("Courier", 9)
            lines = code.split('\n')
            y = 700
            for line in lines[:100]:  # Limit lines per page
                c.drawString(50, y, line[:100])  # Limit line length
                y -= 12
            
            c.save()
            pdf_buffer.seek(0)
            
            return {
                "content": pdf_buffer.getvalue(),
                "format": "pdf",
                "filename": f"{filename}.pdf",
                "mime_type": "application/pdf"
            }
        except Exception as e:
            logger.error(f"PDF creation failed: {str(e)}")
            raise
    
    def _get_extension(self, language: str) -> str:
        """Get file extension for language"""
        extensions = {
            "python": ".py",
            "javascript": ".js",
            "typescript": ".ts",
            "java": ".java",
            "cpp": ".cpp",
            "csharp": ".cs",
            "go": ".go",
            "rust": ".rs",
            "php": ".php",
            "ruby": ".rb",
        }
        return extensions.get(language.lower(), ".txt")
