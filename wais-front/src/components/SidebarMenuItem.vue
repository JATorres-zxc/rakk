<template>
  <div class="sidebar-menu-item">
    <img
      :src="icon"
      :alt="label"
      class="menu-icon"
    />
    <div>{{ label }}</div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'SidebarMenuItem',
  props: {
    icon: {
      type: String,
      required: true,
    },
    label: {
      type: String,
      required: true,
    },
  },
});
</script>

<style scoped>
.sidebar-menu-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 22px;
}

.menu-icon {
  aspect-ratio: 1;
  object-fit: contain;
  object-position: center;
  width: 37px;
}
</style>