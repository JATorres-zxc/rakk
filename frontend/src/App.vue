<script setup lang="ts">
import SideBar from './components/Sidebar.vue'
import HeaderBar from './components/HeaderBar.vue'
import Calendar from './components/Calendar.vue'

</script>



<template>
  <div class="container">
    <!-- Sidebar -->
    <SideBar />
    <Calendar />
    <!-- Main Content (Header and Other Pages) -->
    <div class="main-content">
      <HeaderBar />
    </div>
  </div>
</template>


<style scoped>
  .container {
    display: flex;
    height: 100vh; /* Full height */
  }

  .main-content {
    flex: 1; /* Takes the remaining space */
    display: flex;
    flex-direction: column;
  }
  </style>
