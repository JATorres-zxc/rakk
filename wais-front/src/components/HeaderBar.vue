<script setup lang="ts">
import { SignedIn, SignedOut, SignInButton, UserButton } from '@clerk/vue'
</script>

<template>
  <header class="header-bar">
    <nav class="navigation">
      <a href="#" class="nav-item">
        <img
          src="https://cdn.builder.io/api/v1/image/assets/ecf01e10324340c9995a5c95c87db7a5/5fc0c7d0b9d9820e712b8955c4593741a73ce2a0326597e46524fe8c6eaa9cbb?apiKey=ecf01e10324340c9995a5c95c87db7a5&"
          alt="Dashboard icon"
          class="nav-icon"
        />
        <span class="nav-text">Dashboard</span>
      </a>
      <a href="#" class="nav-item active">
        <img
          src="https://cdn.builder.io/api/v1/image/assets/ecf01e10324340c9995a5c95c87db7a5/f7a186f785f8690b20f39541b75ae76e779fb6e9098d8add23d77e9155a19404?apiKey=ecf01e10324340c9995a5c95c87db7a5&"
          alt="Calendar icon"
          class="nav-icon"
        />
        <span class="nav-text">Calendar</span>
      </a>
    </nav>
    
    <div class="user-actions">
      <header>
    <SignedOut>
      <SignInButton mode='modal'>
      <button class="button">Login</button>
      </SignInButton>
    </SignedOut>
    <SignedIn>
      <UserButton class="userbtn" />
    </SignedIn>
  </header>
    </div>
  </header>
</template>

<script lang="ts">
import { defineComponent } from "vue";


export default defineComponent({
  name: "HeaderBar",
});
</script>

<style scoped>
.header-bar {
  margin-left: 124px;
  z-index: 10;
  display: flex;
  width: 1225.4px;
  max-width: 100%;
  justify-content: space-between;
  padding: 13px 26px 13px 80px;
  border: 1px solid #e0e0e0;
  align-items: center;
}

.navigation {
  display: flex;
  gap: 40px 71px;
  margin: auto 0;
  font: 600 20px Inter, sans-serif;
}
.button {
  margin-top: 10px;
  background: none;
  border: none;
  font: 100 16px Inter, sans-serif;
  color: black;
  cursor: pointer;
  padding: 1;
}
.userbtn {
  width: 40px;
  height: 40px;
}
.button:hover {
  color: blue;
}
.nav-item {
  display: flex;
  gap: 17px;
  color: #000;
  text-decoration: none;
}

.nav-item.active {
  color: #4285f4;
}

.nav-icon {
  aspect-ratio: 1;
  object-fit: contain;
  object-position: center;
  width: 16px;
}

.user-actions {
  display: flex;
  gap: 7px;
}

.user-avatar {
  aspect-ratio: 1;
  object-fit: contain;
  object-position: center;
  width: 51px;
  border-radius: 10px;
}

.notifications-icon {
  aspect-ratio: 1;
  object-fit: contain;
  object-position: center;
  width: 23px;
  margin: auto 0;
}

@media (max-width: 991px) {
  .header-bar {
    padding: 0 20px;
  }
}
</style>
