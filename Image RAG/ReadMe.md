# Image Retrieval Using RAG

This model implements a **Retrieval-Augmented Generation (RAG)** model to query and retrieve relevant images from the **Fashionpedia** dataset. The system utilizes **ChromaDB** as a vector database to store image embeddings, which are generated using **OpenCLIP**. Users can input text queries (e.g., "red tops"), and the system will return the most relevant images from the dataset.

## Features
- **Image Dataset Loading**: Automatically downloads the **Fashionpedia** dataset and saves images locally.
- **ChromaDB Integration**: Stores image embeddings in ChromaDB for fast retrieval.
- **Image Querying**: Allows users to search for relevant images using text queries.
- **RAG Model**: Combines text and image modalities to retrieve relevant images.

## Flow: 
1. **Dataset Loading**: 
   The **Fashionpedia** dataset is downloaded and saved in a local directory (`./images_data`).
   
2. **Image Saving**:
   The code extracts and saves the first 1000 images from the dataset into a folder for further processing.

3. **ChromaDB Initialization**:
   A **ChromaDB** vector database is created to store image embeddings, which are computed using the **OpenCLIP** model.

4. **Image Insertion into ChromaDB**:
   The system iterates through the saved images and adds them to the ChromaDB vector database.

5. **Querying the Database**:
   Users can input a text query, and the system will return the top N relevant images based on the similarity of their embeddings to the text query.

6. **Displaying Results**:
   The relevant images are displayed with their file paths and distances (relevance scores).

Note: 
Before running the file ensure to install the requirements as: 
   ```
   pip install -r requirements.txt
   ```
## Conclusion
This project demonstrates a **Retrieval-Augmented Generation (RAG)** system that combines text and image data to retrieve relevant fashion images using **ChromaDB** and **OpenCLIP**. The approach can be extended to various domains where text-image retrieval is essential.

