<template>
    <div class="custom-time-grid-event">
      <input v-model="isChecked" type="checkbox" />
      <div>Id: {{ calendarEvent.id }}</div>
      <div>Title: {{ calendarEvent.title }}</div>
    </div>
  </template>
  
  <script lang="ts" setup>
  import {ref, watch} from 'vue'
  import type { PropType } from 'vue'
  import {useEventsStore} from "@/stores/events-store";
  
  const props = defineProps({
    calendarEvent: {
      type: Object as PropType<{ title: string; id: number | string }>,
      required: true,
    },
  })
  
  const isChecked = ref(false)
  
  watch(isChecked, () => {
    eventsStore.toggleEvent(props.calendarEvent!.id)
  })
  
  const eventsStore = useEventsStore()
  
  </script>
  
  <style>
  .custom-time-grid-event {
    border: 2px solid black;
    border-radius: 4px;
    background-color: #fff;
    font-family: inherit;
    line-height: 1.5;
    padding: 0.125rem;
    width: 100%;
    height: 100%;
  }
  </style>