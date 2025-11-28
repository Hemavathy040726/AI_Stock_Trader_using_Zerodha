# src/utils/exceptions.py
class AppError(Exception):
    """Base exception for the application"""
    pass

class PDFReadError(AppError):
    pass

class ZerodhaAPIError(AppError):
    pass

class ToolExecutionError(AppError):
    pass

class RetryableError(AppError):
    """Marks errors that should trigger retry"""
    pass