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

            <!-- Multi-Select Market Dropdown -->
            <div class="market-dropdown">
                <label for="market-search">Select Markets:</label>

                <!-- Search Bar -->
                <input type="text" v-model="searchQuery" placeholder="Search markets..." class="search-box" />

                <!-- Dropdown List -->
                <div class="dropdown-list" v-if="filteredMarkets.length > 0">
                    <div v-for="market in filteredMarkets" :key="market" @click="toggleMarketSelection(market)" 
                        :class="['dropdown-item', { 'selected': selectedMarkets.includes(market) }]">
                        {{ market }}
                    </div>
                </div>

                <!-- Selected Markets as Tags -->
                <div class="selected-tags">
                    <span v-for="market in selectedMarkets" :key="market" class="tag">
                        {{ market }}
                        <span class="remove-tag" @click="removeMarket(market)">✖</span>
                    </span>
                </div>

                <!-- Submit Button -->
                <button @click="submitMarkets">Submit Selected Markets</button>
            </div>


            <!-- Date Picker and Prediction Days Input -->
            <div class="prediction-section">
                <label for="prediction-date">Select Date:</label>
                <input type="date" v-model="selectedDate" id="prediction-date" />

                <label for="days-to-predict">Days to Predict:</label>
                <input type="number" v-model="daysToPredict" id="days-to-predict" min="1" />

                <button @click="submitPrediction">Predict</button>
            </div>

            <!-- Submit Button -->
            <button class="submit-btn" @click="submitSelection">Submit</button>

        </div>

        <!-- Floating Sidebar for Submenu -->
        <div v-if="activeIndex !== null" 
            ref="floatingSidebar"
            class="floating-sidebar" 
            :style="{ top: `${sidebarTop}px` }">
            <div class="checkbox-list-header">
                <p class="checkbox-list-title" style="font-weight: bold;">{{ menuItems[activeIndex].name }}</p>
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
import { ref, computed, nextTick } from "vue";
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

const selectedDate = ref("");
const daysToPredict = ref(1);

const submitPrediction = () => {
    if (!selectedDate.value || daysToPredict.value < 1) {
        alert("Please select a valid date and enter a positive number of days.");
        return;
    }

    if (daysToPredict.value > 50) {
        alert("The maximum number of days to predict is 50.");
        daysToPredict.value = 50; // Optionally, reset it to 50
        return;
    }

    // Convert selected date to ISO format
    const isoDate = new Date(selectedDate.value).toISOString();

    const requestData = {
        date: isoDate,
        days: daysToPredict.value,
    };

    console.log("Submitting Prediction Data:", requestData);

    // Send to API
    // fetch('YOUR_BACKEND_ENDPOINT', {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify(requestData)
    // });
};











// Market List from Image
const marketList = ref([
  "Agora Public Market/San Juan",
  "Balintawak (Cloverleaf) Market",
  "Bicutan Market",
  "Blumentritt Market",
  "Cartimar Market",
  "Dagonoy Market",
  "Guadalupe Public Market/Makati",
  "Kamuning Public Market",
  "La Huerta Market/Parañaque",
  "New Las Piñas City Public Market",
  "Malabon Central Market",
  "Mandaluyong Public Market",
  "Marikina Public Market",
  "Maypajo Public Market/Caloocan",
  "Mega Q-mart/Quezon City",
  "Pamilihang Lungsod ng Muntinlupa",
  "Muñoz Market/Quezon City",
  "Murphy Public Market",
  "Navotas Agora Market",
  "New Marulas Public Market/Valenzuela",
  "Paco Market",
  "Pasay City Market",
  "Pasig City Mega Market",
  "Pateros Market",
  "Pritil Market/Manila",
  "Quinta Market/Manila",
  "San Andres Market/Manila",
  "Taguig People’s Market",
  "Trabajo Market"
]);

const selectedMarkets = ref([]);
const searchQuery = ref("");
// Computed property: Filter markets based on search query
const filteredMarkets = computed(() => {
    if (!searchQuery.value) return marketList.value;
    return marketList.value.filter(market => 
        market.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
});

// Toggle market selection
const toggleMarketSelection = (market) => {
    if (selectedMarkets.value.includes(market)) {
        selectedMarkets.value = selectedMarkets.value.filter(m => m !== market);
    } else {
        selectedMarkets.value.push(market);
    }
};

// Remove a selected market
const removeMarket = (market) => {
    selectedMarkets.value = selectedMarkets.value.filter(m => m !== market);
};
// Submit Selected Markets
const submitMarkets = () => {
    if (selectedMarkets.value.length > 0) {
        console.log("Submitting Markets:", selectedMarkets.value);
        // Send to API
        // fetch('YOUR_BACKEND_ENDPOINT', {
        //   method: 'POST',
        //   headers: { 'Content-Type': 'application/json' },
        //   body: JSON.stringify({ markets: selectedMarkets.value })
        // });
    } else {
        alert("Please select at least one market.");
    }
};

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
]);

const activeIndex = ref(null);
const sidebarTop = ref(0);
const floatingSidebar = ref(null);
const selectedIndex = ref(null); // Track the selected menu item

// Submit function
const submitSelection = () => {
  const selectedData = menuItems.value
    .filter(item => item.subMenu.some(sub => sub.checked))
    .map(item => ({
      category: item.name,
      selectedItems: item.subMenu.filter(sub => sub.checked).map(sub => sub.name)
    }));

  console.log("Submitting Data:", selectedData);
  // You can replace this with an actual API call
  // fetch('YOUR_BACKEND_ENDPOINT', {
  //   method: 'POST',
  //   headers: { 'Content-Type': 'application/json' },
  //   body: JSON.stringify(selectedData)
  // });
};

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
.prediction-section {
    margin-top: 20px;
    background: #fff;
    padding: 15px;
    border-radius: 5px;
    width: 250px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.prediction-section label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
}

.prediction-section input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-bottom: 10px;
}

.prediction-section button {
    width: 100%;
    padding: 8px;
    background-color: #28a745;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 4px;
}

.prediction-section button:hover {
    background-color: #218838;
}

.market-dropdown {
    margin-top: 20px;
    background: #fff;
    padding: 15px;
    border-radius: 5px;
    width: 250px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.market-dropdown label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
}

/* Search Box */
.search-box {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-bottom: 10px;
}

/* Dropdown List */
.dropdown-list {
    max-height: 150px;
    overflow-y: auto;
    border: 1px solid #ccc;
    border-radius: 4px;
    background: white;
}

.dropdown-item {
    padding: 8px;
    cursor: pointer;
}

.dropdown-item:hover {
    background-color: #f0f0f0;
}

.dropdown-item.selected {
    background-color: #007bff;
    color: white;
}

/* Selected Markets as Tags */
.selected-tags {
    margin-top: 10px;
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
}

.tag {
    background-color: #007bff;
    color: white;
    padding: 5px 10px;
    border-radius: 15px;
    font-size: 14px;
    display: flex;
    align-items: center;
}

.remove-tag {
    margin-left: 8px;
    cursor: pointer;
    font-weight: bold;
}

.remove-tag:hover {
    color: red;
}

/* Submit Button */
button {
    margin-top: 10px;
    width: 100%;
    padding: 8px;
    background-color: #007bff;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 4px;
}

button:hover {
    background-color: #0056b3;
}
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
    color: black;
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
  border-radius: 7px;
    position: absolute;
    left: 135px;
    width: 160px;
    background: #feffc3;
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