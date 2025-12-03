import { useEffect, useState } from "react";
import Apis, { endpoints } from "../utils/Apis"
import { Chip } from "react-native-paper";
import MyStyles from "../styles/MyStyles";
import { TouchableOpacity, View } from "react-native";



const Catogories = ({ setCateId })=>{
    const [categories, setCategories] = useState([]);


    const loadCates = async()=>{
        let res = await Apis.get(endpoints['categories']);
        setCategories(res.data)

    }
    useEffect (()=>{
        loadCates();
    },[])
    return (
        <View style = {MyStyles.row}>
            <TouchableOpacity onPress={()=> setCateId(null)}>
                <Chip style={MyStyles.margin}  icon='label' >Tất cả</Chip>
            </TouchableOpacity>
            {categories.map(c => <TouchableOpacity key={c.id} onPress={()=> setCateId(c.id)}>
                <Chip style={MyStyles.margin}  icon='label' >{ c.name }</Chip>
            </TouchableOpacity>)}
        </View>
    )
}
export default Catogories