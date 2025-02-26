<template>
    <div class="flex">
        <!-- Main Sidebar -->
        <div class="sidebar">
            <!-- Logo Section -->
            <div class="logo">
                <img src="https://cdn.builder.io/api/v1/image/assets/ecf01e10324340c9995a5c95c87db7a5/e2433d35477616d63912ae308a20a85e61fe58c050f421ac21fd63e5612d5981?apiKey=ecf01e10324340c9995a5c95c87db7a5&" alt="Logo">
            </div>

            <ul>
                <li v-for="(item, index) in menuItems" 
                    :key="index" 
                    @click="toggleSubSidebar(index, $event)"
                    @mouseover="hoverIndex = index"
                    @mouseleave="hoverIndex = null"
                    :class="['menu-item', { 'selected': selectedIndex === index }]">
                    <img :src="hoverIndex === index || selectedIndex === index ? item.hoverIcon : item.icon" 
                        :alt="item.name" width="24" height="24">
                    <span>{{ item.name }}</span>
                </li>
            </ul>

        </div>

        <!-- Floating Sidebar for Submenu -->
        <div v-if="activeIndex !== null" 
            ref="floatingSidebar"
            class="floating-sidebar" 
            :style="{ top: `${sidebarTop}px` }">
            <div class="checkbox-list-header">
                <p class="checkbox-list-title">{{ menuItems[activeIndex].name }}</p>
                <img src="@/assets/icons/chevron_left.png" 
                alt="Close" 
                class="close-btn" 
                @click="closeSidebar">
            </div>
            <ul>
                <li v-for="(subItem, subIndex) in menuItems[activeIndex].subMenu" 
                    :key="subIndex"
                    class="submenu-item">
                    <!-- Bind the checkbox to the checked state -->
                    <input type="checkbox" 
                           :id="`checkbox-${subIndex}`" 
                           v-model="subItem.checked" />
                    <label :for="`checkbox-${subIndex}`">{{ subItem.name }}</label>
                </li>
            </ul>
            
        </div>
    </div>
</template>

<script setup>
import { ref, nextTick } from "vue";
import riceIcon from "@/assets/icons/rice.png";
import fishIcon from "@/assets/icons/fish.png";
import poultryIcon from "@/assets/icons/poultry.png";
import vegetableIcon from "@/assets/icons/vegetable.png";
import sweetenerIcon from "@/assets/icons/sweetener.png";
import othersIcon from "@/assets/icons/others.png";

import riceIconColored from "@/assets/icons/rice_colored.png";
import fishIconColored from "@/assets/icons/fish_colored.png";
import poultryIconColored from "@/assets/icons/poultry_colored.png";
import vegetableIconColored from "@/assets/icons/vegetable_colored.png";
import sweetenerIconColored from "@/assets/icons/sweetener_colored.png";
import othersIconColored from "@/assets/icons/others_colored.png";

const hoverIndex = ref(null);

const menuItems = ref([
  { 
    name: "Rice", 
    icon: riceIcon, 
    hoverIcon: riceIconColored,
    subMenu: [{ name: "Well-milled Rice (Local)", checked: false }]
  },
  { 
    name: "Fish", 
    icon: fishIcon, 
    hoverIcon: fishIconColored,
    subMenu: [{ name: "Tilapia", checked: false }, { name: "Galunggong", checked: false }]
  },
  { 
    name: "Poultry", 
    icon: poultryIcon, 
    hoverIcon: poultryIconColored,
    subMenu: [
      { name: "Fresh Pork Kasim/Pigue", checked: false },
      { name: "Fresh Pork Liempo", checked: false },
      { name: "Fresh Whole Chicken", checked: false },
      { name: "Egg (Medium)", checked: false }
    ]
  },
  { 
    name: "Vegetable", 
    icon: vegetableIcon, 
    hoverIcon: vegetableIconColored,
    subMenu: [
      { name: "Ampalaya", checked: false },
      { name: "Eggplant", checked: false },
      { name: "Tomato", checked: false },
      { name: "Cabbage", checked: false },
      { name: "Red Onion", checked: false }
    ]
  },
  { 
    name: "Sweetener", 
    icon: sweetenerIcon, 
    hoverIcon: sweetenerIconColored,
    subMenu: [{ name: "Sugar (Washed)", checked: false }]
  },
  { 
    name: "Others", 
    icon: othersIcon, 
    hoverIcon: othersIconColored,
    subMenu: [
      { name: "Gas", checked: false }
    ]
  }
]);

const activeIndex = ref(null);
const sidebarTop = ref(0);
const floatingSidebar = ref(null);
const selectedIndex = ref(null); // Track the selected menu item

const toggleSubSidebar = async (index, event) => {
  if (activeIndex.value === index) {
    activeIndex.value = null;
    selectedIndex.value = null; // Unselect when closing
  } else {
    activeIndex.value = index;
    selectedIndex.value = index; // Mark as selected

    // Add flicker effect
    const clickedImage = event.currentTarget.querySelector("img");
    clickedImage.classList.add("flicker");

    // Remove flicker effect after animation ends
    setTimeout(() => {
      clickedImage.classList.remove("flicker");
    }, 300); // Match animation duration

    await nextTick();

    const clickedElement = event.currentTarget;
    const rect = clickedElement.getBoundingClientRect();
    const menuItemCenterY = rect.top + rect.height / 2;
    const floatingSidebarHeight = floatingSidebar.value.offsetHeight;
    const viewportHeight = window.innerHeight;

    let topPosition = menuItemCenterY - floatingSidebarHeight / 2;
    if (topPosition < 65) topPosition = 65;
    if (topPosition + floatingSidebarHeight > viewportHeight - 10) { 
      topPosition = viewportHeight - floatingSidebarHeight - 10;
    }

    sidebarTop.value = topPosition;
  }
};

// Close when clicking the chevron_left button
const closeSidebar = () => {
  activeIndex.value = null;
  selectedIndex.value = null; // Remove selection
};
</script>
<style scoped>
.flex {
    display: flex;
    position: relative;
}

.sidebar {
    width: 125px;
    background: #4A6C2F; /* Match the color from the image */
    color: white;
    padding: 10px;
    text-align: center;
}

/* Logo styling */
.logo img {
    width: 100px;
    margin-bottom: 32px;
    margin-top: 10px;
}

.menu-item {
    position: relative;
    padding: 10px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-align: center;
    width: 100%;
}

.menu-item.selected::after {
    content: "";
    position: absolute;
    right: -10px;
    top: 0;
    height: 80%;
    width: 5px; /* Adjust width as needed */
    background-color: #DAE000;
    border-radius: 5px 0 0 5px;
}

ul {
    padding: 0;
    margin: 0;
    list-style: none;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.menu-item img {
    width: 34px;
    height: 34px;
    margin-bottom: 0px;
    transition: transform 0.2s ease-in-out; /* Smooth transition */
}

.menu-item:hover img,
.menu-item.selected img { 
    transform: scale(1.3); /* Scale up the image */
}

.menu-item span {
    font-size: 16px;
    font-family: Inter, sans-serif;
    color: white;
    margin-bottom: 10px;
}

.menu-item:hover {
    background: transparent; /* No background change */
}

/* Floating Sidebar */
.floating-sidebar {
    position: absolute;
    left: 135px;
    width: 160px;
    background: white;
    padding: 10px;
    border: 1px solid #ccc;
}

/* Submenu Styling */
.submenu-item {
    padding: 5px;
    cursor: pointer;
    text-align: left; /* Align text to the left */
    border-radius: 5px;
    display: flex; /* Use flexbox for alignment */
    align-items: center; /* Vertically center items */
    width: 100%; /* Full width to align left */
    padding: 3px 5px; /* Reduce padding to lower spacing */
    margin: 2px 0; /* Reduce margin to make items closer */
}

.submenu-item input[type="checkbox"] {
    margin-right: 8px; /* Add space between checkbox and label */
}

.submenu-item:hover {
    background: #eee;
}

.checkbox-list-header {
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    margin-bottom: 10px;
}

.checkbox-list-title {
    flex-grow: 1;
    text-align: center;
    font-size: 18px;
}

.close-btn {
    position: absolute;
    right: 0;
    width: 18px;  /* Adjust size as needed */
    height: 18px;
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
}

.close-btn:hover {
    transform: scale(1.2);
}

.submenu-item input[type="checkbox"] {
    accent-color: black;
}

@keyframes flicker {
    0% { opacity: 1; }
    50% { opacity: 0.3; }
    100% { opacity: 1; }
}

.flicker {
    animation: flicker 0.3s ease-in-out;
}

</style>