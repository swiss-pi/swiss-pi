import ToolSeite from '../components/ToolSeite.jsx'

function Cowrie() {
    return (
        <ToolSeite
            titel="Swiss-Pi-Suricata"
            kacheln={[
                { name: 'Angriffe heute', wert: '–' },
                { name: 'Angreifer-IPS', wert: '–' },
                { name: 'Login-Versuche', wert: '–' },
                { name: 'Befehle', wert: '–' },
            ]}
        />
    )
}

export default Cowrie
