<script setup lang="ts">
import Calendar from './components/CalendarDaily.vue';
import CalendarPage from './components/CalendarPage.vue';
import HeaderBar from './components/HeaderBar.vue';
import SidebarMenu from './components/SidebarMenu.vue';

</script>

<template>
  <div class="container">
    <HeaderBar />
    
    <div class="content">
      <SidebarMenu class="sidebar" />
      <Calendar class="calendar" />
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  height: 100vh; /* Full viewport height */
}

.content {
  display: flex;
  flex: 1; /* Takes up remaining space */
}

/* .sidebar {
  width: 250px;
  background-color: #f4f4f4; 
  height: 100%;
  padding: 20px;
} */

.calendar {
  flex: 1; /* Takes up remaining space */
  padding: 20px;
  overflow: auto; /* Prevent overflow issues */
}
</style>
