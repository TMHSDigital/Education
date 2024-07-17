# Machine Learning APIs

## TensorFlow Serving

- **Description**: Provides a flexible, high-performance serving system for machine learning models.
- **URL**: [TensorFlow Serving](https://www.tensorflow.org/tfx/guide/serving)
- **Sample Request**:
```bash
curl -X POST http://localhost:8501/v1/models/your_model:predict -d '{
  instances: [1.0, 2.0, 5.0]
}'
```

## Hugging Face Transformers

- **Description**: Provides access to state-of-the-art machine learning models for NLP tasks.
- **URL**: [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- **Sample Request**:
```bash
curl -X POST https://api-inference.huggingface.co/models/bert-base-uncased -H Authorization: Bearer YOUR_ACCESS_TOKEN -d '{
  inputs: The quick brown fox jumps over the lazy dog.
}'
```

## IBM Watson

- **Description**: Provides a suite of machine learning and AI tools including language processing, visual recognition, and data analysis.
- **URL**: [IBM Watson](https://www.ibm.com/cloud/watson)
- **Sample Request**:
```bash
curl -X POST https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/YOUR_INSTANCE_ID/v1/analyze?version=2019-07-12 -u apikey:YOUR_API_KEY -H Content-Type: application/json -d '{
  text: IBM is an American multinational technology company.,
  features: {
    entities: {},
    keywords: {}
  }
}'
```

## Google Cloud AI

- **Description**: Provides a variety of machine learning APIs including vision, speech, language, and AutoML.
- **URL**: [Google Cloud AI](https://cloud.google.com/products/ai)
- **Sample Request**:
```bash
curl -X POST https://language.googleapis.com/v1/documents:analyzeEntities?key=YOUR_API_KEY -H Content-Type: application/json -d '{
  document: {
    type: PLAIN_TEXT,
    content: Google Cloud provides a range of machine learning APIs.
  }
}'
```

## Microsoft Azure Cognitive Services

- **Description**: Provides a suite of APIs for vision, speech, language, and decision-making.
- **URL**: [Azure Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/)
- **Sample Request**:
```bash
curl -X POST https://YOUR_REGION.api.cognitive.microsoft.com/text/analytics/v3.0/keyPhrases -H Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY -H Content-Type: application/json -d '{
  documents: [
    {
      language: en,
      id: 1,
      text: Microsoft Azure is a cloud computing service created by Microsoft.
    }
  ]
}'
```

