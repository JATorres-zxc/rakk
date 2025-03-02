<template>
    <div class="custom-event-modal">
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
  .custom-event-modal {
    background-color: pink;
    color: cornflowerblue;
    font-weight: 700;
  }
  </style>