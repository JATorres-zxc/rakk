<template>
  <nav class="sidebar-menu">
    <img
      src="https://cdn.builder.io/api/v1/image/assets/ecf01e10324340c9995a5c95c87db7a5/e2433d35477616d63912ae308a20a85e61fe58c050f421ac21fd63e5612d5981?apiKey=ecf01e10324340c9995a5c95c87db7a5&"
      alt="Logo"
      class="logo"
    />
    <SidebarMenuItem
      icon="/src/assets/icons/rice.png"
      hoverIcon="/src/assets/icons/rice_colored.png"
      label="Rice"
      :selected="selectedLabel === 'Rice'"
      @update:selectedLabel="toggleSelection"
    />
    <SidebarMenuItem
      icon="/src/assets/icons/corn.png"
      hoverIcon="/src/assets/icons/corn_colored.png"
      label="Corn"
      :selected="selectedLabel === 'Corn'"
      @update:selectedLabel="toggleSelection"
    />
    <SidebarMenuItem
      icon="/src/assets/icons/poultry.png"
      hoverIcon="/src/assets/icons/poultry_colored.png"
      label="Poultry"
      :selected="selectedLabel === 'Poultry'"
      @update:selectedLabel="toggleSelection"
    />
    <SidebarMenuItem
      icon="/src/assets/icons/fish.png"
      hoverIcon="/src/assets/icons/fish_colored.png"
      label="Fish"
      :selected="selectedLabel === 'Fish'"
      @update:selectedLabel="toggleSelection"
    />
    <SidebarMenuItem
      icon="/src/assets/icons/vegetable.png"
      hoverIcon="/src/assets/icons/vegetable_colored.png"
      label="Vegetable"
      :selected="selectedLabel === 'Vegetable'"
      @update:selectedLabel="toggleSelection"
    />
    <SidebarMenuItem
      icon="/src/assets/icons/fruits.png"
      hoverIcon="/src/assets/icons/fruits_colored.png"
      label="Fruit"
      :selected="selectedLabel === 'Fruit'"
      @update:selectedLabel="toggleSelection"
    />
    <SidebarMenuItem
      icon="/src/assets/icons/spices.png"
      hoverIcon="/src/assets/icons/spices_colored.png"
      label="Spices"
      :selected="selectedLabel === 'Spices'"
      @update:selectedLabel="toggleSelection"
    />
    <SidebarMenuItem
      icon="/src/assets/icons/others.png"
      hoverIcon="/src/assets/icons/others_colored.png"
      label="Others"
      :selected="selectedLabel === 'Others'"
      @update:selectedLabel="toggleSelection"
    />
  </nav>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import SidebarMenuItem from "@/components/SidebarMenuItem.vue";

export default defineComponent({
  name: "SidebarMenu",
  components: { SidebarMenuItem },
  setup() {
    const selectedLabel = ref<string | null>(null);

    // Toggle selection logic
    const toggleSelection = (label: string | null) => {
      selectedLabel.value = selectedLabel.value === label ? null : label;
    };

    return { selectedLabel, toggleSelection };
  },
});
</script>

<style scoped>
.sidebar-menu {
  margin-top: -79px;
  background-color: #4a6c2f;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  align-items: center;
  color: #f5e8c7;
  width: 124px;
  max-width: 100%;
  padding: 40px 13px;
  font: 300 14px Inter, sans-serif;
}

.logo {
  aspect-ratio: 4.31;
  object-fit: contain;
  object-position: center;
  width: 100%;
  align-self: stretch;
  margin-top: -10px;
  margin-bottom: 40px;
}

.decorative-image {
  aspect-ratio: 1.22;
  object-fit: contain;
  object-position: center;
  width: 66px;
  margin-top: 26px;
}

@media (max-width: 991px) {
  .sidebar-menu {
    white-space: initial;
  }
}
</style>