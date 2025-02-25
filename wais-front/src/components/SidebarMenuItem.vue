<template>
  <div 
    class="sidebar-menu-item" 
    @mouseover="isHovered = true" 
    @mouseleave="isHovered = false" 
    @click="handleClick"
    :class="{ 'clicked': isClicked, 'flicker': shouldFlicker }"
  >
    <img :src="isHovered || isClicked ? hoverIcon : icon" :alt="label" class="menu-icon" />
    <span class="menu-label">{{ label }}</span>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, watch } from "vue";

export default defineComponent({
  name: "SidebarMenuItem",
  props: {
    icon: { type: String, required: true },
    hoverIcon: { type: String, required: true },
    label: { type: String, required: true },
    selected: { type: Boolean, required: true },
  },
  setup(props, { emit }) {
    const isHovered = ref(false);
    const shouldFlicker = ref(false);

    const isClicked = computed(() => props.selected);

    const handleClick = () => {
      const newSelection = props.selected ? null : props.label;
      emit("update:selectedLabel", newSelection);

      shouldFlicker.value = true;
      setTimeout(() => {
        shouldFlicker.value = false;
      }, 300);
    };

    // Watch for `selected` prop changes and reset hover state
    watch(() => props.selected, (newValue) => {
      if (!newValue) {
        isHovered.value = false;
      }
    });

    return { isHovered, isClicked, shouldFlicker, handleClick };
  },
});
</script>




<style scoped>
.sidebar-menu-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 25px;
  cursor: pointer;
  padding-left: 0px;
  transition: border-left 0.3s ease-in-out;
  position: relative;
  width: 100%;
  text-align: center;
}

.sidebar-menu-item.clicked::after {
  content: "";
  position: absolute;
  top: -8px;
  right: -12.5px;
  width: 4px;
  height: 120%;
  background-color: #DAE000;
}


.menu-icon {
  width: 20px;
  height: 20px;
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.sidebar-menu-item:hover .menu-icon, 
.sidebar-menu-item.clicked .menu-icon {
  transform: scale(1.7);
  opacity: 1;
}

.menu-label {
  margin-top: 8px;
  font-size: 14px;
  color: #f5e8c7;
}

/* Flicker animation using opacity */
@keyframes flicker {
  0% { opacity: 1; } /* Start at full opacity */
  50% { opacity: 0.5; } /* Lower opacity halfway */
  100% { opacity: 1; } /* Return to full opacity */
}

.flicker .menu-icon {
  animation: flicker 0.3s ease;
}
</style>