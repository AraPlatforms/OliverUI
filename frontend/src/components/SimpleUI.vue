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
    
    <div v-if="isLoading" class="loading-container">
      <div class="coffee-mug">
        <div class="coffee"></div>
      </div>
      <p>Oliver is brewing your critique. This usually takes about 20 seconds.</p>
      <p>He's probably sipping an artisanal coffee while judging your site.</p>
    </div>
    
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

export default {
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

.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 2rem;
}

.coffee-mug {
  width: 100px;
  height: 80px;
  background-color: #ffffff;
  border: 5px solid #34495e;
  border-radius: 0 0 50px 50px;
  position: relative;
  margin-bottom: 20px;
}

.coffee-mug::before {
  content: '';
  position: absolute;
  right: -20px;
  top: 15px;
  width: 25px;
  height: 40px;
  border: 5px solid #34495e;
  border-left: none;
  border-radius: 0 25px 25px 0;
}

.coffee {
  width: 100%;
  height: 0;
  background-color: #3498db;
  position: absolute;
  bottom: 0;
  border-radius: 0 0 45px 45px;
  animation: fill 2s ease-in-out infinite;
}

@keyframes fill {
  0%, 100% { height: 0; }
  50% { height: 70%; }
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
}

.markdown-content ul {
  list-style-type: none;
  padding-left: 0;
}

.markdown-content li {
  margin-bottom: 0.5rem;
  padding-left: 1.5rem;
  position: relative;
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
</style>