<script>
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        isWSConnected: false,
        history: [],
        username: null
    },
    mutations: {
        pushMessage(state, message){
            state.history.push(message);
        },
        setUsername(state, username){
            state.username = username;
        },
        wsConnect(state){
            state.isWSConnected = true;
        },
        wsDisconnect(state){
            state.isWSConnected = false;
        }
    }
});
</script>
