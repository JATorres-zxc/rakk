<script setup lang="ts">
import { ScheduleXCalendar } from '@schedule-x/vue'
import {
  createCalendar,
  viewMonthAgenda,
  viewMonthGrid,
} from '@schedule-x/calendar'
import '@schedule-x/theme-default/dist/index.css'
import {createScrollControllerPlugin} from "@schedule-x/scroll-controller";
import {createEventRecurrencePlugin, createEventsServicePlugin} from "@schedule-x/event-recurrence";
import {createEventModalPlugin} from "@schedule-x/event-modal";

import { calendars } from "../calendars";
import { shallowRef } from "vue";
import type { CSSProperties } from "vue";
import {createCalendarControlsPlugin} from "@schedule-x/calendar-controls";
import { events } from "../data/events";
import { faAlignCenter } from '@fortawesome/free-solid-svg-icons';


const eventsService = createEventsServicePlugin();
const calendarControls = createCalendarControlsPlugin();
const eventModal = createEventModalPlugin();

const calendarApp = shallowRef(createCalendar({
  selectedDate: new Date().toISOString().split('T')[0],
  locale: 'en-UK',
  views: [viewMonthAgenda, viewMonthGrid],
  defaultView: viewMonthGrid.name,
  calendars: calendars,
  plugins: [
    eventModal,
    createScrollControllerPlugin({
      initialScroll: '07:00'
    }),
    createEventRecurrencePlugin(),
    eventsService,
    calendarControls
  ],
  events: events,
  monthGridOptions: {
    nEventsPerDay: 3,
  },
  callbacks: {
    onClickDate(date) {
      calendarControls.setView(viewMonthGrid.name);
      calendarControls.setDate(date);
    }
  }
}))

const closeModal = () => {
  eventModal.close();
}

const formatDateRange = (start:string, end:string) => {
  const startDate = new Date(start).toLocaleDateString('en-UK', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });

  const endDate = new Date(end).toLocaleDateString('en-UK', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });

  return startDate === endDate ? startDate : `${startDate} - ${endDate}`;
};


const eventStyles: CSSProperties = {
  width: '100%',
  height: '100%',
  backgroundColor: '#FDFDE4',
  borderRadius: '4px',
  marginLeft: '10px',
}

const eventModalStyles: CSSProperties = {
  width: "60vw",
  maxWidth: "90vw",
  maxHeight: "80vh",
  backgroundColor: "#feffaf",
  border: "2px solid black",
  borderRadius: "8px",
  padding: "1rem",
  boxShadow: "0 0 2em #123",
  overflow: "hidden",
};



</script>

<template>
  <div>
    <ScheduleXCalendar 
        style="display: inline-block; text-align: center; margin: auto;"
        :calendar-app="calendarApp"
    >
      <template #dateGridEvent="{ calendarEvent }">
        <div :style="eventStyles">
          {{ calendarEvent.title }}
        </div>
      </template>

      <template #timeGridEvent="{ calendarEvent }">
        <div :style="eventStyles">
          {{ calendarEvent.title }}
        </div>
      </template>

      <template #monthGridEvent="{ calendarEvent }">
        <div class="event-box">
          {{ calendarEvent.title }}
        </div>
      </template>

      <template #eventModal="{ calendarEvent }">
  <div class="modal-container">
    <div :style="eventModalStyles">
      <div style="position: relative; display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
        <p style="font-weight: bold; font-size: large; margin: 0; flex-grow: 1; text-align: center;">
          {{ formatDateRange(calendarEvent.start, calendarEvent.end) }}
        </p>
        <button @click="closeModal" class="close-button">
          <img src="@/assets/close-icon.png" alt="Close" />
        </button>
      </div>

      <div class="event-modal-content">
      <table>
        <thead class="sticky-header">
          <tr>
            <th>Item</th>
            <th>Best Date to Buy</th>
            <th>Price This Day</th>
            <th>Place to Buy</th>
          </tr>
        </thead>
        <tbody class="scrollable-body">
          <tr v-for="item in calendarEvent.items" :key="item.name">
            <td>
              <input type="checkbox" />
              {{ item.name }}
            </td>
            <td>{{ item.bestDate }}</td>
            <td>₱{{ item.price.toFixed(2) }}</td>
            <td>{{ item.placeToBuy }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    </div>
  </div>
  
</template>



    </ScheduleXCalendar>
  </div>
</template>

<style scoped>
table {
  width: 100%; /* Ensures the table takes full width */
  border-collapse: collapse; /* Ensures proper spacing */
}

th, td {
  padding: 10px; /* Adds spacing inside cells */
  text-align: left; /* Aligns text to center */
}

th {
  width: 33.33%; /* Distributes columns equally */
}

th:nth-child(1), td:nth-child(1) { /* Item Column */
  width: 40%;
}

th:nth-child(2), td:nth-child(2) { /* Best Date to Buy Column */
  width: 20%;
}

th:nth-child(3), td:nth-child(3) { /* Price This Day Column */
  width: 20%;
}

th:nth-child(4), td:nth-child(4) { /* Place to Buy Column */
  width: 20%;
}

th:nth-child(1) { /* Center only the "Item" header */
  text-align: center;
}

td:nth-child(1) { /* Keep the items left-aligned */
  text-align: left;
}

.close-button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  position: sticky;
  top: 0; /* Stick to the top */
  right: 0;
  z-index: 10; /* Ensure it stays above other content */
}

.close-button img {
  width: 15px;
  height: 15px;
  transition: transform 0.2s ease-in-out;
}

.close-button:hover img {
  transform: scale(1.2);
}

/* Ensure modal content scrolls without affecting close button */
.event-modal-content {
  max-height: 70vh; /* Limit height */
  overflow-y: auto; /* Enable scrolling */
  padding-top: 0px; /* Ensure content doesn't overlap the sticky button */
  padding-right: 10px;
}

.modal-container {
  position: fixed;
  top: 0;
  left: 0;
  width: calc(100% - 335px); /* Adjust for sidebar */
  height: calc(100% - 60px); /* Adjust for header */
  margin-left: 250px; /* Push right from sidebar */
  margin-top: 60px; /* Push down from header */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999; /* Ensure it appears on top */
}
.sticky-header {
  position: sticky;
  top: 0;
  background: rgb(254, 255, 175); /* Ensure background remains visible */
  z-index: 10; /* Keeps it above scrollable content */
  color: rgb(0, 0, 0);
}

.scrollable-body {
  display: table-row-group; /* Ensures proper table layout */
  max-height: 200px;
  overflow-y: auto;
}

input[type="checkbox"] {
  accent-color: black;
}

.event-box {
  width: 100%;
  height: 100%;
  background-color: #FDFDE4;
  border-radius: 4px;
  margin-left: 10px;
  transition: background-color 0.3s ease-in-out;
}

.event-box:hover {
  background-color: rgb(254, 255, 175);
}

</style>