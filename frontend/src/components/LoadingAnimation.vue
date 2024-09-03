<!-- LoadingAnimation.vue -->
<template>
    <div class="loading-container">
      <div class="typewriter">{{ displayText }}</div>
      <p>Oliver is analyzing your site. This usually takes about 20 seconds.</p>
      <p>He's probably sipping an artisanal coffee while judging your design.</p>
    </div>
  </template>
  
  <script>
  import { ref, onMounted, onUnmounted } from 'vue'
  
  export default {
    name: 'LoadingAnimation',
    setup() {
      const displayText = ref('')
      const fullText = 'Critiquing...'
      let index = 0
      let intervalId = null
  
      const animateText = () => {
        intervalId = setInterval(() => {
          if (index >= fullText.length) {
            index = 0
            displayText.value = ''
          } else {
            index++
            displayText.value = fullText.slice(0, index)
          }
        }, 200)
      }
  
      onMounted(() => {
        animateText()
      })
  
      onUnmounted(() => {
        clearInterval(intervalId)
      })
  
      return {
        displayText
      }
    }
  }
  </script>
  
  <style scoped>
  .loading-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 2rem;
  }
  
  .typewriter {
    font-family: monospace;
    font-size: 2em;
    color: #3498db;
    margin-bottom: 1rem;
    min-height: 1.2em;
  }
  </style>