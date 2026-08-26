import sys

# Context Detection: Check if we are running under Streamlit
is_streamlit = ('streamlit' in sys.modules) or any('streamlit' in arg for arg in sys.argv)

if is_streamlit:
    # 1. STREAMLIT MODE: Run the actual learning hub Streamlit code
    import streamlit_app
else:
    # 2. VERCEL MODE: Serve the app via Flask in a fast static-wrapper iframe
    from flask import Flask, render_template_string
    
    app = Flask(__name__)
    
    @app.route('/')
    @app.route('/<path:path>')
    def serve_iframe(path=""):
        return render_template_string('''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>IP Dict XI: AI Learning Hub</title>
                <style>
                    body, html {
                        margin: 0;
                        padding: 0;
                        height: 100%;
                        overflow: hidden;
                        background-color: #07080e;
                    }
                    iframe {
                        width: 100%;
                        height: 100%;
                        border: none;
                    }
                </style>
            </head>
            <body>
                <iframe src="https://pydict.streamlit.app/?embed=true"></iframe>
            </body>
            </html>
        ''')
        
    if __name__ == '__main__':
        app.run(port=3000)
