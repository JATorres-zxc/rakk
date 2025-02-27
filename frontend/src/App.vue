<script setup lang="ts">
import SideBar from './components/Sidebar.vue'
import HeaderBar from './components/HeaderBar.vue'
import Calendar from './components/Calendar.vue'
</script>

<template>
  <div class="container">
    <!-- Sidebar (Fixed on the Left) -->
    <SideBar class="sidebar" />

    <div class="main-content">
      <!-- HeaderBar (Blue) -->
      <HeaderBar class="header-bar" />

      <!-- Calendar (Yellow) -->
      <div class="calendar-wrapper">
        <Calendar />
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Sidebar: Fixed on the left */
.sidebar {
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh; /* Full height */
  width: 130px;
  z-index: 1000; /* Keeps it on top */
}

/* Main Content Wrapper */
.main-content {
  margin-left: 130px; /* Matches sidebar width */
  margin-top: 60px; /* Matches header height */
  display: flex;
  flex-direction: column;
  height: calc(100vh - 60px);
  overflow: hidden;
}

.header-bar {
  position: fixed; /* Fixes it to the top */
  top: 0;
  left: 130px; /* To avoid overlapping the sidebar */
  right: 0;
  height: 60px; /* Adjust as needed */
  background: white; /* Ensure visibility */
  z-index: 1100; /* Higher than sidebar and calendar */
  display: flex;
  align-items: center;
  padding: 0 20px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Optional shadow */
}


.calendar-wrapper {
  flex-grow: 1;
  overflow: auto;
  width: 100%;
}
</style>
