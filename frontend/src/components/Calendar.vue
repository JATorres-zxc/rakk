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


const eventsService = createEventsServicePlugin();
const calendarControls = createCalendarControlsPlugin();
const eventModal = createEventModalPlugin();

const calendarApp = shallowRef(createCalendar({
  selectedDate: '2025-02-25',
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
  events: [
    {
      id: 1,
      start: '2025-02-28',
      end: '2025-02-28',
      title: 'hi',
      calendarId: 'work',
    },
    {
      id: 2,
      start: '2024-06-28 08:00',
      end: '2024-06-28 10:00',
      title: 'hi again',
      calendarId: 'work',
    },
    {
  id: 3,
  start: '2025-02-22',
  end: '2025-02-22',
  title: 'Chicken Egg',
  calendarId: 'shopping',
  items: [
    { name: 'Tilapia', bestDate: '12-February-2025', price: 160.00 },
    { name: 'Rice', bestDate: '10-February-2025', price: 45.00 },
    { name: 'Ginger', bestDate: '19-February-2025', price: 190.00 },
    { name: 'Egg', bestDate: '28-February-2025', price: 8.00 },
    { name: 'Tomato', bestDate: '18-February-2025', price: 60.00 },
    { name: 'Sugar', bestDate: '04-February-2025', price: 75.00 },
    { name: 'Pork Belly', bestDate: '10-February-2025', price: 460.00 },
    { name: 'Galunggong', bestDate: '22-February-2025', price: 300.00 }
  ]
}

  ],
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


const eventStyles = {
  width: '100%',
  height: '100%',
  backgroundColor: 'white',
  border: '2px solid black',
  borderRadius: '4px',
  padding: '0 4px',
}

const eventModalStyles: CSSProperties = {
  boxShadow: "0 0 2em #123",
  backgroundColor: "#feffaf", // Light yellowish background
  border: "2px solid black",
  borderRadius: "8px",
  padding: "1rem",
  width: "500px",
  maxWidth: "90vw",
  maxHeight: "80vh",
  overflowY: "auto", // Ensure this is a valid CSS value
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
        <div :style="eventStyles">
          {{ calendarEvent.title }}
        </div>
      </template>

      <template #eventModal="{ calendarEvent }">
  <div :style="eventModalStyles">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
      <p style="font-weight: bold; font-size: large; margin: 0; flex-grow: 1; text-align: center;">
        {{ formatDateRange(calendarEvent.start, calendarEvent.end) }}
      </p>
      <button @click="closeModal" class="close-button">
        <img src="@/assets/close-icon.png" alt="Close" />
      </button>
    </div>

    <table>
      <thead>
        <tr>
          <th>Item</th>
          <th>Best Date to Buy</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in calendarEvent.items" :key="item.name">
          <td>
            <input type="checkbox" />
            {{ item.name }}
          </td>
          <td>{{ item.bestDate }}</td>
          <td>₱{{ item.price.toFixed(2) }}</td>
        </tr>
      </tbody>
    </table>
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
  text-align: center; /* Aligns text to center */
}

th {
  width: 33.33%; /* Distributes columns equally */
}

.close-button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}

.close-button img {
  width: 15px;
  height: 15px;
  transition: transform 0.2s ease-in-out;
}

.close-button:hover img {
  transform: scale(1.2); /* Increases size by 20% */
}
</style>