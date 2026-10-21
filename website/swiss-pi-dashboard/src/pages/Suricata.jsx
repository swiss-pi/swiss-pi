import ToolSeite from '../components/ToolSeite.jsx'

function Suricata() {
    return (
        <ToolSeite
            titel="Swiss-Pi-Suricata"
            kacheln={[
                { name: 'Alert', wert: '–' },
                { name: 'Critical', wert: '–' },
                { name: 'High', wert: '–' },
                { name: 'Status', wert: '–' },
            ]}
        />
    )
}

export default Suricata