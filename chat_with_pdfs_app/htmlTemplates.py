css = '''
<style>
/* Global Styles */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

/* Main Container Styling */
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Header Styling */
h1 {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 700;
    font-size: 2.5rem;
    text-align: center;
    margin-bottom: 2rem;
    text-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

/* Sidebar Styling */
.sidebar .sidebar-content {
    background: linear-gradient(180deg, #f8fafc 0%, #e2e8f0 100%);
    border-radius: 20px;
    padding: 1.5rem;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    border: 1px solid rgba(255,255,255,0.2);
}

.sidebar h3 {
    color: #1e293b;
    font-weight: 600;
    margin-bottom: 1rem;
    font-size: 1.2rem;
}

/* File Uploader Styling */
.stFileUploader {
    background: white;
    border-radius: 15px;
    padding: 1rem;
    border: 2px dashed #cbd5e1;
    transition: all 0.3s ease;
}

.stFileUploader:hover {
    border-color: #667eea;
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.2);
}

/* Comprehensive File Uploader Text Styling */
.stFileUploader * {
    color: #1e293b !important;
}

/* File Uploader Container */
.stFileUploader > div {
    color: #1e293b !important;
}

/* File Uploader Text Elements */
.stFileUploader p, .stFileUploader span, .stFileUploader div {
    color: #1e293b !important;
}

/* File Names Display */
.stFileUploader [data-testid="stFileUploaderFile"] {
    background: #f8fafc !important;
    color: #1e293b !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 8px !important;
    padding: 0.5rem !important;
    margin: 0.25rem 0 !important;
}

/* Upload Button */
.stFileUploader button:not([data-testid="stFileUploaderDelete"]) {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.5rem 1rem !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

.stFileUploader button:not([data-testid="stFileUploaderDelete"]):hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3) !important;
}

/* Delete File Button */
.stFileUploader [data-testid="stFileUploaderDelete"] {
    background: #ef4444 !important;
    color: white !important;
    border: none !important;
    border-radius: 4px !important;
    padding: 0.25rem 0.5rem !important;
    font-size: 0.75rem !important;
    transition: all 0.3s ease !important;
}

.stFileUploader [data-testid="stFileUploaderDelete"]:hover {
    background: #dc2626 !important;
    transform: scale(1.05) !important;
}

/* Drop Zone Text */
.stFileUploader [data-testid="stFileUploaderDropZone"] {
    color: #64748b !important;
}

/* File Uploader Status Text */
.stFileUploader [data-testid="stFileUploaderStatus"] {
    color: #1e293b !important;
    font-weight: 500 !important;
}

/* Force all text in file uploader to be visible */
.stFileUploader, .stFileUploader *, .stFileUploader *::before, .stFileUploader *::after {
    color: #1e293b !important;
}

/* Exception for buttons that should be white text */
.stFileUploader button {
    color: white !important;
}

/* Exception for delete buttons */
.stFileUploader [data-testid="stFileUploaderDelete"] {
    color: white !important;
}

/* Button Styling */
.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.75rem 2rem;
    font-weight: 600;
    font-size: 1rem;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    width: 100%;
    margin-top: 1rem;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

/* Text Input Styling */
.stTextInput > div > div > input {
    border-radius: 12px;
    border: 2px solid #e2e8f0;
    padding: 1rem;
    font-size: 1rem;
    transition: all 0.3s ease;
    background: white;
}

.stTextInput > div > div > input:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    outline: none;
}

/* Chat Message Styling */
.chat-message {
    padding: 1.5rem;
    border-radius: 20px;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    animation: slideIn 0.5s ease-out;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
}

.chat-message:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.12);
}

.chat-message.user {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    margin-left: 2rem;
    border-bottom-right-radius: 5px;
}

.chat-message.bot {
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    margin-right: 2rem;
    border-bottom-left-radius: 5px;
    border: 1px solid #e2e8f0;
}

.chat-message .avatar {
    width: 50px;
    height: 50px;
    flex-shrink: 0;
    position: relative;
}

.chat-message .avatar img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid white;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.chat-message .avatar img:hover {
    transform: scale(1.1);
}

.chat-message .message {
    flex: 1;
    padding: 0;
    color: #1e293b;
    font-size: 1rem;
    line-height: 1.6;
    font-weight: 400;
}

.chat-message.user .message {
    color: white;
    font-weight: 500;
}

/* Success/Error Messages */
.stSuccess {
    background: #d1fae5;
    color: #065f46;
    border-radius: 12px;
    padding: 1rem;
    margin: 1rem 0;
    box-shadow: 0 4px 15px rgba(16, 185, 129, 0.2);
    border: 2px solid #10b981;
    font-weight: 600;
}

.stError {
    background: #fee2e2;
    color: #991b1b;
    border-radius: 12px;
    padding: 1rem;
    margin: 1rem 0;
    box-shadow: 0 4px 15px rgba(239, 68, 68, 0.2);
    border: 2px solid #ef4444;
    font-weight: 600;
}

.stWarning {
    background: #fef3c7;
    color: #92400e;
    border-radius: 12px;
    padding: 1rem;
    margin: 1rem 0;
    box-shadow: 0 4px 15px rgba(245, 158, 11, 0.2);
    border: 2px solid #f59e0b;
    font-weight: 600;
}

/* Spinner Styling */
.stSpinner > div {
    border: 3px solid #e2e8f0;
    border-top: 3px solid #667eea;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    animation: spin 1s linear infinite;
}

/* Hide loading text */
.stSpinner {
    display: flex;
    align-items: center;
    justify-content: center;
}

.stSpinner > div:not(:first-child) {
    display: none !important;
}

.stSpinner p, .stSpinner span, .stSpinner div:not(:first-child) {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
}

/* Animations */
@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* Responsive Design */
@media (max-width: 768px) {
    .chat-message {
        margin-left: 0.5rem;
        margin-right: 0.5rem;
        padding: 1rem;
    }
    
    .chat-message .avatar {
        width: 40px;
        height: 40px;
    }
    
    .chat-message .avatar img {
        width: 40px;
        height: 40px;
    }
    
    h1 {
        font-size: 2rem;
    }
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #f1f5f9;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
}

/* Loading Animation */
.loading-dots {
    display: inline-block;
}

.loading-dots::after {
    content: '';
    animation: dots 1.5s steps(5, end) infinite;
}

@keyframes dots {
    0%, 20% { content: ''; }
    40% { content: '.'; }
    60% { content: '..'; }
    80%, 100% { content: '...'; }
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
