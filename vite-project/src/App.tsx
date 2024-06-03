
import './App.css'

function App() {
  function methodDoesNotExist(): void {
    throw new Error('Function not implemented.')
  }

  return (
    <>
      <h1>Vite + React + Sentry</h1>
      <div style={{display:'flex', alignItems:'flex-start', flexDirection:'column'}}>
        <h2>Sentry Configurations</h2>
        <h3>ENV: "{window.configs.environment}"</h3>
        <h3>Trace Propagation Targets: "{window.configs.tracePropagationTargets.join(', ')}"</h3>
        <h3>PROJECT-ID: "{window.configs.sentryProjectId}"</h3>
        <h3>Key: "XXXXXXXXXXXX{window.configs.sentryKey.substring(12)}"</h3>
      </div>
      <div className="card">
       <button onClick={() => methodDoesNotExist()}>Break the world</button>
      </div>
    </>
  )
}

export default App
