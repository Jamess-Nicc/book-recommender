<script setup lang="ts">
import { ref } from 'vue'

interface Book {
  isbn13: string
  title: string
  authors: string
  categories: string
  description: string
  thumbnail: string
  average_rating: number | null
}

const query = ref('')
const minRating = ref<number | ''>('')
const numberOfBooks = ref(5)

const books = ref<Book[]>([])
const loading = ref(false)
const errorMessage = ref('')

async function searchBooks() {
  if (!query.value.trim()) {
    return
  }

  loading.value = true
  errorMessage.value = ''
  books.value = []

  try {
    const response = await fetch('/api/recommend', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        query: query.value.trim(),
        k: numberOfBooks.value,
        min_rating: minRating.value === '' ? null : minRating.value,
      }),
    })

    if (!response.ok) {
      const errorData = await response.json().catch(() => null)

      throw new Error(
        errorData?.detail ?? 'Unable to retrieve book recommendations.',
      )
    }

    const data = await response.json()

    books.value = data.recommendations
  } catch (error) {
    errorMessage.value =
      error instanceof Error
        ? error.message
        : 'Something went wrong. Please try again.'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <main class="page">
    <header class="header">
      <a class="brand" href="/">
        <span class="brand-icon">B</span>
        <span>BookFinder</span>
      </a>

      <span class="header-label">Semantic Book Discovery</span>
    </header>

    <section class="hero">
      <p class="eyebrow">YOUR NEXT GREAT READ</p>

      <h1>
        Find books that
        <span>understand you.</span>
      </h1>

      <p class="hero-description">
        Describe the story, atmosphere, or ideas you're looking for.
        Discover books that match your interests.
      </p>

      <form class="search-panel" @submit.prevent="searchBooks">
        <label for="query">What would you like to read?</label>

        <textarea
          id="query"
          v-model="query"
          placeholder="A magical adventure about friendship, courage, and discovering a hidden world..."
          rows="3"
          required
          minlength="3"
          maxlength="500"
        ></textarea>

        <div class="filters">
          <div class="filter-group">
            <label for="rating">Minimum rating</label>

            <select id="rating" v-model="minRating">
              <option value="">Any rating</option>
              <option :value="3">3.0+</option>
              <option :value="3.5">3.5+</option>
              <option :value="4">4.0+</option>
              <option :value="4.5">4.5+</option>
            </select>
          </div>

          <div class="filter-group">
            <label for="count">Recommendations</label>

            <select id="count" v-model.number="numberOfBooks">
              <option :value="3">3 books</option>
              <option :value="5">5 books</option>
              <option :value="10">10 books</option>
              <option :value="20">20 books</option>
            </select>
          </div>
        </div>

        <button class="search-button" type="submit">
          Find my next read
          <span aria-hidden="true">→</span>
        </button>
      </form>

      <div v-if="loading" class="status-message" role="status">
  Finding books that match your interests...
</div>

<div v-else-if="errorMessage" class="error-message" role="alert">
  {{ errorMessage }}
</div>

<section v-if="books.length > 0" class="results-section">
  <div class="results-heading">
    <div>
      <p class="eyebrow">YOUR PERSONALIZED RESULTS</p>
      <h2>Books worth exploring</h2>
    </div>

    <span class="results-count">
      {{ books.length }} books
    </span>
  </div>

  <div class="book-list">
    <article
      v-for="(book, index) in books"
      :key="book.isbn13 || `${book.title}-${index}`"
      class="book-card"
    >
      <img
        v-if="book.thumbnail"
        :src="book.thumbnail"
        :alt="`Cover of ${book.title}`"
        class="book-cover"
        loading="lazy"
      />

      <div v-else class="book-cover-placeholder">
        No cover
      </div>

      <div class="book-info">
        <h3>{{ book.title }}</h3>

        <p class="book-author">
          {{ book.authors || 'Unknown author' }}
        </p>

        <p class="book-rating">
          ★
          {{
            book.average_rating != null
              ? book.average_rating.toFixed(2)
              : 'Not rated'
          }}
        </p>

        <p v-if="book.categories" class="book-category">
          {{ book.categories }}
        </p>

        <p class="book-description">
          {{ book.description }}
        </p>
      </div>
    </article>
  </div>
</section>

      <p class="helper-text">
        Powered by semantic search and a collection of 5,197 books.
      </p>
    </section>

    <footer class="footer">
      <span>BookFinder</span>
      <span>Built with Vue, FastAPI, and semantic search.</span>
    </footer>
  </main>
</template>

<style>
:root {
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont,
    "Segoe UI", sans-serif;
  color: #20251f;
  background: #f7f8f4;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-width: 320px;
  min-height: 100vh;
}

button,
textarea,
select {
  font: inherit;
}

.page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.header {
  width: min(1120px, calc(100% - 48px));
  margin: 0 auto;
  padding: 28px 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #e6e9e0;
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  color: inherit;
  text-decoration: none;
  font-size: 19px;
  font-weight: 750;
  letter-spacing: -0.6px;
}

.brand-icon {
  width: 35px;
  height: 35px;
  display: grid;
  place-items: center;
  border-radius: 11px;
  background: #315d43;
  color: white;
}

.header-label {
  color: #737b71;
  font-size: 13px;
}

.hero {
  width: min(720px, calc(100% - 40px));
  margin: 0 auto;
  padding: 76px 0 64px;
  flex: 1;
  text-align: center;
}

.eyebrow {
  margin-bottom: 18px;
  color: #52765a;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 2.2px;
}

h1 {
  margin: 0;
  font-size: clamp(38px, 7vw, 64px);
  line-height: 1.08;
  letter-spacing: -3px;
}

h1 span {
  display: block;
  color: #52765a;
}

.hero-description {
  max-width: 530px;
  margin: 22px auto 36px;
  color: #70776d;
  font-size: 16px;
  line-height: 1.8;
}

.search-panel {
  padding: 26px;
  border: 1px solid #e4e8de;
  border-radius: 20px;
  background: #ffffff;
  text-align: left;
  box-shadow: 0 14px 45px rgb(32 48 32 / 5%);
}

.search-panel label {
  display: block;
  margin-bottom: 10px;
  font-size: 13px;
  font-weight: 700;
}

textarea,
select {
  width: 100%;
  border: 1px solid #e1e5dc;
  border-radius: 10px;
  background: #fbfcf9;
  color: #20251f;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}

textarea {
  min-height: 110px;
  padding: 14px;
  resize: vertical;
  line-height: 1.6;
}

textarea::placeholder {
  color: #9ba197;
}

textarea:focus,
select:focus {
  border-color: #52765a;
  box-shadow: 0 0 0 3px rgb(82 118 90 / 12%);
}

.filters {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-top: 22px;
}

.filter-group select {
  height: 44px;
  padding: 0 12px;
  cursor: pointer;
}

.search-button {
  width: 100%;
  min-height: 49px;
  margin-top: 24px;
  padding: 12px 18px;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  border: 0;
  border-radius: 10px;
  background: #315d43;
  color: #ffffff;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s, transform 0.2s;
}

.search-button:hover {
  background: #264a35;
  transform: translateY(-1px);
}

.search-button:focus-visible {
  outline: 3px solid #9dbda3;
  outline-offset: 3px;
}

.helper-text {
  margin-top: 20px;
  color: #899085;
  font-size: 12px;
}

.footer {
  width: min(1120px, calc(100% - 48px));
  margin: 0 auto;
  padding: 22px 0;
  display: flex;
  justify-content: space-between;
  gap: 16px;
  border-top: 1px solid #e6e9e0;
  color: #81877e;
  font-size: 12px;
}

@media (max-width: 600px) {
  .header {
    width: calc(100% - 32px);
    padding: 20px 0;
  }

  .header-label {
    font-size: 11px;
  }

  .hero {
    padding-top: 54px;
  }

  h1 {
    letter-spacing: -1.8px;
  }

  .search-panel {
    padding: 18px;
  }

  .filters {
    grid-template-columns: 1fr;
    gap: 14px;
  }

  .footer {
    width: calc(100% - 32px);
    flex-direction: column;
    text-align: center;
  }
}

.status-message,
.error-message {
  margin-top: 24px;
  padding: 16px;
  border-radius: 12px;
  font-size: 14px;
}

.status-message {
  background: #edf3eb;
  color: #315d43;
}

.error-message {
  background: #fff0ef;
  color: #a52e2e;
}

.results-section {
  margin-top: 48px;
  text-align: left;
}

.results-heading {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  margin-bottom: 20px;
}

.results-heading .eyebrow {
  margin-bottom: 8px;
}

.results-heading h2 {
  margin: 0;
  font-size: 26px;
  letter-spacing: -0.8px;
}

.results-count {
  color: #737b71;
  font-size: 13px;
  white-space: nowrap;
}

.book-list {
  display: grid;
  gap: 16px;
}

.book-card {
  display: flex;
  align-items: flex-start;
  gap: 20px;
  padding: 20px;
  border: 1px solid #e4e8de;
  border-radius: 16px;
  background: #fff;
}

.book-cover,
.book-cover-placeholder {
  width: 100px;
  min-width: 100px;
  height: 145px;
  border-radius: 6px;
  object-fit: cover;
}

.book-cover-placeholder {
  display: grid;
  place-items: center;
  background: #edf0e9;
  color: #737b71;
  font-size: 12px;
}

.book-info {
  min-width: 0;
}

.book-info h3 {
  margin: 0 0 6px;
  font-size: 19px;
  line-height: 1.4;
}

.book-author {
  margin: 0 0 10px;
  color: #70776d;
  font-size: 13px;
}

.book-rating {
  margin: 0 0 10px;
  color: #8a6a21;
  font-size: 13px;
  font-weight: 700;
}

.book-category {
  margin: 0 0 10px;
  color: #52765a;
  font-size: 12px;
}

.book-description {
  margin: 0;
  color: #70776d;
  font-size: 13px;
  line-height: 1.7;
}

@media (max-width: 480px) {
  .book-card {
    gap: 12px;
    padding: 14px;
  }

  .book-cover,
  .book-cover-placeholder {
    width: 76px;
    min-width: 76px;
    height: 112px;
  }

  .book-info h3 {
    font-size: 16px;
  }
}
</style>