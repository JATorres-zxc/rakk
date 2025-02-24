<template>
  <div class="calendar-page">
    <SidebarMenu />
    <div class="main-content">
      <HeaderBar />
      <div class="calendar-container">
        <div class="calendar-sidebar left"></div>
        <CalendarGrid />
        <div class="calendar-sidebar right"></div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import SidebarMenu from "@/components/SidebarMenu.vue";
import HeaderBar from "./HeaderBar.vue";
import CalendarGrid from "./CalendarGrid.vue";

export default defineComponent({
  name: "CalendarPage",
  components: {
    CalendarGrid,
  },
});
</script>

<style scoped>
.calendar-page {
  background-color: #fff;
  display: flex;
  overflow: hidden;
  flex-wrap: wrap;
}

.main-content {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  flex-basis: 0;
  width: fit-content;
}

.calendar-container {
  display: flex;
  flex-wrap: wrap;
}

.calendar-sidebar {
  background-color: rgba(207, 223, 218, 0.5);
  width: 130px;
  height: 694px;
}

.calendar-sidebar.right {
  height: 692px;
}

@media (max-width: 991px) {
  .main-content {
    max-width: 100%;
  }
}
</style>
