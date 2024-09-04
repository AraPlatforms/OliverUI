<template>
  <div class="container">
    <h1 class="title">Website Design Evaluation</h1>
    <p class="subtitle">Get insightful feedback on your website's design</p>
    
    <blockquote class="quote">
      "Good design is obvious. Great design is transparent." - Joe Sparano
    </blockquote>
    
    <form @submit.prevent="submitWebsite">
      <label for="websiteUrl">Enter your website URL for evaluation:</label>
      <div class="input-group">
        <input
          id="websiteUrl"
          v-model="websiteUrl"
          type="url"
          required
          placeholder="https://example.com"
        >
        <button type="submit" :disabled="isLoading">
          {{ isLoading ? 'Analyzing...' : 'Evaluate My Website' }}
        </button>
      </div>
    </form>
    
    <LoadingAnimation v-if="isLoading" />
    
    <div v-else-if="critique" class="critique-container">
      <div class="critique-header">
        <h2>Design Evaluation Results</h2>
        <button @click="resetForm" class="reset-button">Evaluate Another Site</button>
      </div>
      <div v-html="formattedCritique" class="markdown-content"></div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
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
        console.error("Error during evaluation:", error)
        critique.value = "We apologize, but an error occurred during the evaluation process. Please try again later."
      } finally {
        isLoading.value = false
      }
    }

    const resetForm = () => {
      websiteUrl.value = ''
      critique.value = null
    }

    onMounted(() => {
      document.title = "Website Design Evaluation Tool"
    })

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
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.title {
  font-size: 2.5rem;
  font-weight: bold;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.subtitle {
  font-size: 1.25rem;
  color: #5a6c7d;
  margin-bottom: 1.5rem;
}

.quote {
  font-style: italic;
  color: #34495e;
  background-color: #ecf0f1;
  padding: 1rem;
  border-radius: 4px;
  margin: 1.5rem 0;
  border-left: 4px solid #3498db;
}

form {
  margin-top: 2rem;
}

label {
  display: block;
  font-size: 1.1rem;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

input {
  padding: 0.75rem;
  font-size: 1rem;
  border: 1px solid #bdc3c7;
  border-radius: 4px;
  width: 100%;
}

button {
  padding: 0.75rem 1rem;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover:not(:disabled) {
  background-color: #2980b9;
}

button:disabled {
  background-color: #bdc3c7;
  cursor: not-allowed;
}

.critique-container {
  margin-top: 2rem;
}

.critique-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.reset-button {
  font-size: 0.9rem;
  padding: 0.5rem 1rem;
  background-color: #95a5a6;
}

.reset-button:hover {
  background-color: #7f8c8d;
}

.markdown-content {
  background-color: #f9f9f9;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
  text-align: left;
}
</style>