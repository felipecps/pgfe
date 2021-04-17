<template>
    <div>
        <b-breadcrumb :items="items">
            <b-breadcrumb-item class="" v-for="(item, i) in items" :key="i" :to="item.to">{{item.text}}</b-breadcrumb-item>
        </b-breadcrumb>
    </div>
</template>

<script>
    export default {
        props: {
            items: { type: Array, required: true },
        }
    }
</script>