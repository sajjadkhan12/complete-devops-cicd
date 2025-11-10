<template>
  <div id="app">
    <h1>🎭 Microservices Frontend</h1>
    <div class="container">
      <!-- Poem Service -->
      <div class="card">
        <h2>📜 Random Poem</h2>
        <button @click="fetchPoem" :disabled="loadingPoem">
          {{ loadingPoem ? 'Loading...' : 'Get Random Poem' }}
        </button>
        <div class="content">
          <div v-if="loadingPoem" class="loading">Loading poem...</div>
          <div v-else-if="poemError" class="error">{{ poemError }}</div>
          <div v-else-if="poem" class="poem-content">
            <h3>{{ poem.title }}</h3>
            <p>{{ poem.poem }}</p>
            <div class="author">— {{ poem.author }}</div>
          </div>
          <div v-else>Click the button to get a random poem!</div>
        </div>
      </div>

      <!-- Quote Service -->
      <div class="card">
        <h2>💬 Random Quote</h2>
        <button @click="fetchQuote" :disabled="loadingQuote">
          {{ loadingQuote ? 'Loading...' : 'Get Random Quote' }}
        </button>
        <div class="content">
          <div v-if="loadingQuote" class="loading">Loading quote...</div>
          <div v-else-if="quoteError" class="error">{{ quoteError }}</div>
          <div v-else-if="quote" class="quote-content">
            <p>"{{ quote.quote }}"</p>
            <div class="author">— {{ quote.author }}</div>
            <span class="category">{{ quote.category }}</span>
          </div>
          <div v-else>Click the button to get a random quote!</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      poem: null,
      quote: null,
      loadingPoem: false,
      loadingQuote: false,
      poemError: null,
      quoteError: null
    }
  },
  methods: {
    async fetchPoem() {
      this.loadingPoem = true
      this.poemError = null
      try {
        // Use environment variable or default to relative path (for nginx proxy)
        const apiUrl = import.meta.env.VITE_POEM_API_URL || '/api/poem'
        const url = apiUrl.startsWith('http') ? `${apiUrl}/poem` : `${apiUrl}/poem`
        const response = await axios.get(url)
        this.poem = response.data
      } catch (error) {
        this.poemError = `Error fetching poem: ${error.message}. Make sure the poem microservice is running.`
        console.error('Error fetching poem:', error)
      } finally {
        this.loadingPoem = false
      }
    },
    async fetchQuote() {
      this.loadingQuote = true
      this.quoteError = null
      try {
        // Use environment variable or default to relative path (for nginx proxy)
        const apiUrl = import.meta.env.VITE_QUOTE_API_URL || '/api/quote'
        const url = apiUrl.startsWith('http') ? `${apiUrl}/quote` : `${apiUrl}/quote`
        const response = await axios.get(url)
        this.quote = response.data
      } catch (error) {
        this.quoteError = `Error fetching quote: ${error.message}. Make sure the quote microservice is running.`
        console.error('Error fetching quote:', error)
      } finally {
        this.loadingQuote = false
      }
    }
  }
}
</script>

