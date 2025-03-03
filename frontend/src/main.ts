import './assets/main.css'

// import './style.css'
import '@fontsource/open-sans'
import '@fontsource/open-sans/300.css'
import '@fontsource/open-sans/500-italic.css'
import '@fontsource/open-sans/700.css'
import '@fontsource/open-sans/700-italic.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { clerkPlugin } from '@clerk/vue'

import App from './App.vue'
import router from './router'

const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

if (!PUBLISHABLE_KEY) {
  throw new Error('Add your Clerk Publishable Key to the .env file')
}

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(clerkPlugin, { publishableKey: PUBLISHABLE_KEY })

app.mount('#app')
