PROMPT_TEMPLATE = 'You are a web security expert. Classify each HTTP request as "Normal" or "Anomalous" and provide a brief reason.\n\nExamples:\nRequest: GET /index.jsp HTTP/1.1\nOutput: {{"label": "Normal", "reason": "Standard page request, no suspicious pattern"}}\n\nRequest: GET /search?q=\' OR \'1\'=\'1 HTTP/1.1\nOutput: {{"label": "Anomalous", "reason": "Classic SQL Injection pattern with OR 1=1"}}\n\nNow classify:\nRequest: {http_text}\nOutput:'

LLM 정확도: 0.8300
LLM F1:    0.8211
분류 실패(Unknown): 1건

              precision    recall  f1-score   support

      Normal       0.90      0.79      0.84        56
   Anomalous       0.76      0.89      0.82        44

    accuracy                           0.83       100
   macro avg       0.83      0.84      0.83       100
weighted avg       0.84      0.83      0.83       100

PROMPT_TEMPLATE = 'You are a cybersecurity analyst. Analyze the HTTP request and return label, confidence_score (0~100), and reason. Request: {http_text} Output:'


'You are a cybersecurity analyst. Analyze the HTTP request and return label, confidence_score (0~100), and reason. Request: {http_text} Output:'


LLM 정확도: 0.5600
LLM F1:    0.0000
분류 실패(Unknown): 100건

              precision    recall  f1-score   support

      Normal       0.56      1.00      0.72        56
   Anomalous       0.00      0.00      0.00        44

    accuracy                           0.56       100
   macro avg       0.28      0.50      0.36       100
weighted avg       0.31      0.56      0.40       100
