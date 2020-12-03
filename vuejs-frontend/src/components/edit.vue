<template>
    <div id="update">
        <h1>Update</h1>

        <p><router-link :to="{ name: 'AllData' }">back</router-link></p>

        <notification v-bind:notifications="notifications"></notification>

        <form v-on:submit.prevent="editEmployee">
            <div class="form-group">
                <label name="employee_name">Name employee</label>
                <input type="text" class="form-control" v-model="employee.name_employee" id="employee.name_employee">
            </div>

            <div class="form-group">
                <label name="employee_division">Division</label>
                <input type="text" class="form-control" v-model="employee.division" id="employee.division" required>
            </div>

            <div class="form-group">
                <label name="employee_thumbnail">Thumbnail</label>
                <div v-if="!image">
                Select an image
                        <input type="file" class="form-control" @change="onFileChange">
                </div>
                <div v-else>
                    <img :src="image" />
                    <button @click="removeImage">Remove image</button>
                </div>
            </div>

            <div class="form-group">
                <button class="btn btn-primary">Update</button>
            </div>
        </form>
    </div>
</template>

<script>
    import Notification from './notifications.vue';
    export default{
        data(){
            return{
                employee:{},
                notifications:[],
                image: ''
            }
        },
        created: function(){
            this.getEmployee();
        },
        methods: {
            onFileChange(e) {
            var files = e.target.files || e.dataTransfer.files;
            if (!files.length)
                return;
            this.employee.file = files[0]; 
            this.createImage(files[0]);
            },
            createImage(file) {
                var image = new Image();
                var reader = new FileReader();
                var vm = this;

                reader.onload = (e) => {
                    vm.image = e.target.result;
            };
                reader.readAsDataURL(file);
            },
                removeImage: function (e) {
                this.image = '';
            },
            getEmployee: function()
            {
                this.$http.get('http://localhost:5000/employee/' + this.$route.params.id).then((response) => {
                    this.employee = response.body;
                    this.image = this.employee.thumbnail;
                }, (response) => {
                });
            },
            editEmployee: function()
            {
                var formData = new FormData();
                formData.append('name_employee', this.employee.name_employee);
                formData.append('division', this.employee.division);
                formData.append('file', this.employee.file);
                if(this.notifications) this.notifications = [];
                if(this.image) this.$http.put('http://localhost:5000/employee/' + this.$route.params.id, formData, {
                    headers : {
                        // 'Division-Type' : 'multipart/form-data'
                        'enctype' : 'multipart/form-data'
                    }
                }).then((response) => {
                    this.notifications.push({
                        type: 'success',
                        message: 'Employee updated successfully'
                    });
                }, (response) => {
                    this.notifications.push({
                        type: 'error',
                        message: 'Employee not updated'
                    });
                });
            }
        },
        components: {
            'notification' : Notification
        }
    }
</script>

<style scoped>
img {
  width: 60%;
  margin: auto;
  display: block;
  margin-bottom: 10px;
}
button {
  
}
#update {
    width: 400px;
    margin: 0px 0px 0px 0px;
    margin-top: 0px;
    margin-bottom: 100px;
    margin-right: 80px;
    margin-left: 600px;
}
</style>