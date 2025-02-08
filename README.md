# 🚀 Ollama Hugging Face API

## 🌍 Overview
This guide walks you through deploying an `LLM-based API` using Ollama on Hugging Face Spaces, ensuring seamless global accessibility and performance.

---

## 📌 Deployment Steps

### 1️⃣ Create a New Space
- Navigate to **Hugging Face → Spaces → New Space**.  
- Select **"Docker"** as the SDK.

### 2️⃣ Clone the Space Repository
- Clone the repository to your local environment for easy file uploads.  
- Run the following command in your terminal:
  ```sh
  git clone your_space_url
  ```

### 3️⃣ Upload Project Files
- Copy **`app.py`**, **`Dockerfile`**, and **`requirements.txt`** into your project folder.  
- The default model used is **`llama3.1`**, but you can modify it as needed.  
- If changing the model, update its name in both **`Dockerfile`** and **`app.py`**.  
- ⚠️ Be mindful of computational constraints—Hugging Face Spaces primarily run on CPUs.

### 4️⃣ Commit and Push Changes
- Commit and push your updates to the Hugging Face repository.
- The deployment process will **automatically build and launch** the Space.
- Monitor the **Build Logs** tab for any potential errors.

### 5️⃣ Validate API Functionality
- Access your deployed API via:
  ```
  https://username-space_name.hf.space/docs
  ```
- Use `/` for a quick check and `/chat` to test LLM interactions.

---

## ✅ Best Practices & Considerations
✔️ If experiencing **memory issues**, consider using a **lighter LLM model**.  
✔️ Regularly check Hugging Face documentation for **resource updates and optimizations**.  
✔️ Ensure **`requirements.txt`** includes all necessary dependencies to prevent build failures.  
✔️ Implement **robust error handling** in `app.py` to improve API reliability.  

---

## 🔗 Repository Access  
Explore the API repository here: [🚀 Ollama Hugging Face API](https://firass-ollama.hf.space/docs#/).