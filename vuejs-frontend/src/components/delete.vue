<template>
    <div id="delete-product">
        <h1>Delete Employee {{ employee.name_employee }}</h1>

        <p><router-link :to="{ name: 'AllData' }">Back</router-link></p>

        <notification v-bind:notifications="notifications"></notification>

        <form v-on:submit.prevent="deleteEmployee">
            <p><button class="btn btn-danger">Delete Employee</button></p>
        </form>
    </div>
</template>

<script>
    import Notification from './notifications.vue';

    export default{
        data(){
            return{
                employee:{},
                notifications:[]
            }
        },

        created: function(){
            this.getEmployee();
        },

        methods: {
            getEmployee: function()
            {
                this.$http.get('http://localhost:5000/employee/' + this.$route.params.id).then((response) => {
                    this.employee = response.body;
                }, (response) => {

                });
            },

            deleteEmployee: function()
            {
                if(this.notifications) this.notifications = [];
                this.$http.delete('http://localhost:5000/employee/' + this.$route.params.id, this.employee, {
                    headers : {
                        'Division-Type' : 'application/json'
                    }
                }).then((response) => {
                    this.$router.push({name: 'AllData'})
                }, (response) => {
                    this.notifications.push({
                        type: 'danger',
                        message: 'Employee could not deleted'
                    });
                });
            }
        },

        components: {
            'notification' : Notification
        }
    }
</script>