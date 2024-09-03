<template>
  <div class="container">
    <h1>Oliver's Website Critique</h1>
    <p class="subtitle">Prepare your UI for a hipster-grade roasting</p>
    <p class="quote">"I've seen better designs scribbled on napkins at artisanal coffee shops." - Oliver</p>
    
    <hr>
    
    <div v-if="!critique">
      <form @submit.prevent="submitWebsite">
        <label for="websiteUrl">Enter your soon-to-be-roasted website URL:</label>
        <div class="input-group">
          <input
            id="websiteUrl"
            v-model="websiteUrl"
            type="url"
            required
            placeholder="https://example.com"
          >
          <button type="submit" :disabled="isLoading">
            {{ isLoading ? 'Brewing critique...' : 'Roast My Website' }}
          </button>
        </div>
      </form>
    </div>
    
    <LoadingAnimation v-if="isLoading" />
    
    <div v-else-if="critique" class="critique-container">
      <div class="critique-header">
        <h2>Oliver's Verdict</h2>
        <button @click="resetForm" class="reset-button">Evaluate Another Site</button>
      </div>
      <div v-html="formattedCritique" class="markdown-content"></div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import axios from 'axios'
import { marked } from 'marked'
import LoadingAnimation from './LoadingAnimation.vue'

export default {
  components: {
    LoadingAnimation
  },
  setup() {
    const websiteUrl = ref('')
    const isLoading = ref(false)
    const critique = ref(null)

    const formattedCritique = computed(() => {
      return critique.value ? marked(critique.value) : ''
    })

    const submitWebsite = async () => {
      isLoading.value = true
      try {
        const response = await axios.post('http://localhost:8000/api/critique', {
          url: websiteUrl.value,
          description: "No description provided"
        })
        critique.value = response.data.markdown_report
      } catch (error) {
        console.error("Error during critique:", error)
        critique.value = "Oops! It seems Oliver had one too many artisanal coffees. Please try again later."
      } finally {
        isLoading.value = false
      }
    }

    const resetForm = () => {
      websiteUrl.value = ''
      critique.value = null
    }

    return {
      websiteUrl,
      isLoading,
      critique,
      formattedCritique,
      submitWebsite,
      resetForm
    }
  }
}
</script>

<style scoped>
body {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
}

.container {
  text-align: center;
  background-color: white;
  border-radius: 8px;
  padding: 2rem;
}

h1 {
  color: #2c3e50;
  font-size: 2.5em;
  margin-bottom: 0.2em;
}

.subtitle {
  color: #7f8c8d;
  font-size: 1.2em;
  margin-top: 0;
}

.quote {
  font-style: italic;
  color: #34495e;
  background-color: #ecf0f1;
  padding: 1rem;
  border-radius: 4px;
  margin: 1rem 0;
  border-left: 4px solid #3498db;
}

hr {
  border: none;
  border-top: 1px solid #eee;
  margin: 20px 0;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.input-group {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 500px;
  margin-top: 10px;
}

input {
  padding: 10px;
  font-size: 16px;
  border: 1px solid #bdc3c7;
  border-radius: 4px;
  margin-bottom: 10px;
}

button {
  padding: 10px 20px;
  background-color: #3498db;
  color: white;
  border: none;
  cursor: pointer;
  font-size: 16px;
  border-radius: 4px;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #2980b9;
}

button:disabled {
  background-color: #bdc3c7;
  cursor: not-allowed;
}

.critique-container {
  text-align: left;
}

.critique-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.reset-button {
  font-size: 0.9em;
  padding: 8px 16px;
  background-color: #e74c3c;
  color: white;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.reset-button:hover {
  background-color: #c0392b;
}

.markdown-content {
  background-color: #f9f9f9;
  border-radius: 8px;
  padding: 2rem;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
}

.markdown-content h1 {
  font-size: 2em;
  color: #2c3e50;
  border-bottom: 2px solid #3498db;
  padding-bottom: 0.5rem;
  margin-bottom: 1rem;
}

.markdown-content h2 {
  font-size: 1.5em;
  color: #34495e;
  margin-top: 1.5rem;
}

.markdown-content p {
  margin-bottom: 1rem;
  color: #7f8c8d;
}

.markdown-content ul {
  list-style-type: none;
  padding-left: 0;
}

.markdown-content li {
  margin-bottom: 0.5rem;
  padding-left: 1.5rem;
  position: relative;
  color: #34495e;
}

.markdown-content li::before {
  content: '•';
  color: #3498db;
  font-weight: bold;
  position: absolute;
  left: 0;
}

.markdown-content strong {
  color: #e74c3c;
  font-weight: 600;
}

.markdown-content em {
  color: #27ae60;
  font-style: italic;
}

.markdown-content blockquote {
  border-left: 4px solid #8e44ad;
  padding-left: 1rem;
  margin: 1rem 0;
  color: #8e44ad;
  font-style: italic;
}

.markdown-content code {
  background-color: #f1c40f;
  color: #2c3e50;
  padding: 0.2rem 0.4rem;
  border-radius: 4px;
  font-family: 'Courier New', Courier, monospace;
}

.markdown-content a {
  color: #3498db;
  text-decoration: none;
  border-bottom: 1px dashed #3498db;
  transition: color 0.3s;
}

.markdown-content a:hover {
  color: #2980b9;
}
</style>
