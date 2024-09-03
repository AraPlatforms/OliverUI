<template>
  <div class="container">
    <header class="hero">
      <img :src="require('@/assets/oliver_ui_hero.png')" alt="Oliver Hero Image" class="hero-image">
      <h1>Your Website’s Brutally Honest, Yet Insightful Critic</h1>
    </header>

    <main class="content">
      <section v-if="!isLoading && !critiqueReceived" id="submission" class="grid-section">
        <h2>Submit Your Website</h2>
        <form @submit.prevent="submitUrl">
          <input type="text" v-model="websiteUrl" placeholder="Enter your website URL" required>
          <button type="submit" class="cta-button">Critique My Website</button>
        </form>
      </section>

      <section v-if="isLoading" id="loading" class="grid-section">
        <div class="loader"></div>
        <p>Analyzing your website... Get ready for some tough love!</p>
      </section>

      <section v-if="critiqueReceived" id="critique" class="grid-section">
        <h2>Oliver's Critique</h2>
        <div id="critiqueText" v-html="critiqueText"></div>
        <button @click="shareOnTwitter" class="cta-button">Share on Twitter</button>
      </section>
    </main>
  </div>
</template>

<script>
import axios from 'axios';
import { marked } from 'marked';

export default {
  data() {
    return {
      websiteUrl: '',
      isLoading: false,
      critiqueReceived: false,
      critiqueText: '',
      oliverImage: 'src/assets/oliver_ui_hero.png', // Adjusted the image path
    };
  },
  methods: {
    async submitUrl() {
      this.isLoading = true;
      this.critiqueReceived = false;

      try {
        const response = await axios.post('http://localhost:8000/api/critique', {
          url: this.websiteUrl,
          description: "Website critique by Oliver"
        });

        const critique = response.data.critique;
        const markdownReport = response.data.markdown_report;

        this.critiqueText = this.generateCritiqueText(critique, markdownReport);
        this.critiqueReceived = true;
      } catch (error) {
        console.error("Error during critique:", error);
        alert("There was an error processing your request.");
      } finally {
        this.isLoading = false;
      }
    },
    generateCritiqueText(critique, markdownReport) {
      const urlLink = `<a id="websiteLink" href="${this.websiteUrl}" target="_blank">${this.websiteUrl}</a>`;
      const report = marked.parse(markdownReport); // Convert markdown to HTML
      return `<div>${urlLink}, ${critique.summary}</div><div id="report">${report}</div>`;
    },
    shareOnTwitter() {
      const tweetText = encodeURIComponent(this.critiqueText.replace(/<\/?[^>]+(>|$)/g, "")); // Strip HTML tags
      const twitterUrl = `https://twitter.com/intent/tweet?text=${tweetText}`;
      window.open(twitterUrl, "_blank");
    }
  }
};
</script>

<style scoped>
body {
  font-family: 'Helvetica Neue', sans-serif;
  background-color: #fdf6e3;
  color: #333;
  margin: 0;
  padding: 20px;
}

.container {
  max-width: 700px;
  margin: 0 auto;
  background-color: #ffffff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}

.hero {
  position: relative;
  text-align: center;
  color: #ffffff;
  padding: 40px;
  border-radius: 8px;
  background: #4A7A9D;
}

.hero-image {
  max-width: 100%;
  border-radius: 8px;
  margin-bottom: 20px;
}

h1 {
  font-size: 2.5em;
  margin-bottom: 0.5em;
  font-weight: bold;
}

.content {
  display: grid;
  gap: 20px;
  margin-top: 20px;
}

.grid-section {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fafafa;
}

h2 {
  font-size: 2em;
  color: #3e3b2f;
  margin-bottom: 15px;
}

input[type="text"] {
  width: calc(100% - 130px);
  padding: 12px;
  border: 2px solid #9e8c75;
  border-radius: 4px;
  background-color: #fdfdfd;
  color: #5b4636;
  margin-bottom: 15px;
  transition: border-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

input[type="text"]:focus {
  border-color: #4A7A9D;
  box-shadow: 0 0 8px rgba(74, 122, 157, 0.5);
}

input[type="text"]::placeholder {
  color: #9e8c75;
}

.cta-button {
  padding: 12px 30px;
  background-color: #786951;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out, transform 0.1s ease-in-out;
}

.cta-button:hover {
  background-color: #665744;
  transform: scale(1.05);
}

.cta-button:active {
  transform: scale(0.95);
}

#loading .loader {
  border: 5px solid #f3f3f3;
  border-radius: 50%;
  border-top: 5px solid #786951;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
  margin: 20px auto;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

#critiqueText {
  font-style: italic;
  text-align: left;
  margin-bottom: 20px;
  color: #4A7A9D;
}

#websiteLink {
  color: #4A7A9D;
  text-decoration: none;
  font-weight: bold;
}

#websiteLink:hover {
  text-decoration: underline;
}

#report {
  padding: 15px;
  background-color: #ffffff;
  border-radius: 8px;
  color: #4f3c2b;
  margin-top: 20px;
  font-family: 'Georgia', serif;
}

#report h1,
#report h2,
#report h3 {
  color: #4A7A9D;
  border-bottom: 2px solid #4A7A9D;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

#report p {
  margin: 10px 0;
}

#report a {
  color: #4A7A9D;
  text-decoration: none;
}

#report a:hover {
  text-decoration: underline;
}

pre {
  background-color: #f4f0e6;
  padding: 10px;
  border-radius: 4px;
  color: #5b4636;
  overflow-x: auto;
}
</style>
