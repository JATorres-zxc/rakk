<script setup>
import { ScheduleXCalendar } from '@schedule-x/vue'
import {
  createCalendar,
  createViewMonthGrid,
} from '@schedule-x/calendar'
import '@schedule-x/theme-default/dist/index.css'
 
const calendarApp = createCalendar({
  selectedDate: '2025-02-19',
  views: [
    createViewMonthGrid(),
  ],
  events: [
    {
      id: 1,
      title: 'Chicken Egg',
      start: '2025-02-19',
      end: '2025-02-19',
    },
    {
      id: 2,
      title: 'Well-Milled Rice',
      start: '2025-02-07',
      end: '2025-02-07',
    },
    {
      id: 3,
      title: 'Corn',
      start: '2025-02-07',
      end: '2025-02-07',
    },
  ],
})
</script>
 
<template>
  <div>
    <ScheduleXCalendar :calendar-app="calendarApp" />
  </div>
</template>