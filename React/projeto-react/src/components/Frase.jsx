import styles from './Frase.module.css'

function Frase(){
    return(
        <div className={styles.frase_container}>
            <p className={styles.fraseContent}>este componente é uma frase</p>
        </div>
    )
}
export default Frase