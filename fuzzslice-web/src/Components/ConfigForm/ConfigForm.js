import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './ConfigForm.css';

const ConfigForm = () => {
  const [config, setConfig] = useState(null); // Initialize with null to indicate loading state
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetchConfig();
  }, []);

  const fetchConfig = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/config');
      setConfig(response.data);
    } catch (error) {
      console.error('Error fetching config:', error);
      setMessage('Error fetching configuration.');
    }
  };

  const handleInputChange = (e) => {
    const { name, value, type, checked } = e.target;
    setConfig({
      ...config,
      [name]: type === 'checkbox' ? checked : (type === 'number' ? parseFloat(value) : value),
    });
  };

  const handleUpdateConfig = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/config', config);
      setConfig(response.data);
      setMessage('Configuration updated successfully!');
    } catch (error) {
      console.error('Error updating config:', error);
      setMessage('Error updating configuration.');
    }
  };

  if (!config) {
    return <div>Loading...</div>; // Display a loading state while fetching data
  }

  return (
    <div>
      <h1>Configuration Manager</h1>
      {message && <p>{message}</p>}
      <form onSubmit={handleUpdateConfig}>
        <div>
          <label>
            Bug Timeline Targets Run:
            <input
              type="checkbox"
              name="bug_timeline_targets_run"
              checked={config.bug_timeline_targets_run}
              onChange={handleInputChange}
            />
          </label>
        </div>
        <div>
          <label>
            Crash Limit:
            <input
              type="number"
              name="crash_limit"
              value={config.crash_limit}
              onChange={handleInputChange}
            />
          </label>
        </div>
        <div>
          <label>
            Fuzz Tool:
            <input
              type="number"
              name="fuzz_tool"
              value={config.fuzz_tool}
              onChange={handleInputChange}
            />
          </label>
        </div>
        <div>
          <label>
            Hard Timeout:
            <input
              type="number"
              name="hard_timeout"
              value={config.hard_timeout}
              onChange={handleInputChange}
            />
          </label>
        </div>
        <div>
          <label>
            Log Report:
            <input
              type="checkbox"
              name="log_report"
              checked={config.log_report}
              onChange={handleInputChange}
            />
          </label>
        </div>
        <div>
          <label>
            Max Length Fuzz Bytes:
            <input
              type="number"
              name="max_length_fuzz_bytes"
              value={config.max_length_fuzz_bytes}
              onChange={handleInputChange}
            />
          </label>
        </div>
        <div>
          <label>
            Parallel Execution:
            <input
              type="checkbox"
              name="parallel_execution"
              checked={config.parallel_execution}
              onChange={handleInputChange}
            />
          </label>
        </div>
        <div>
          <label>
            Test Library:
            <input
              type="text"
              name="test_library"
              value={config.test_library}
              onChange={handleInputChange}
            />
          </label>
        </div>
        <div>
          <label>
            Timeout:
            <input
              type="number"
              name="timeout"
              value={config.timeout}
              onChange={handleInputChange}
            />
          </label>
        </div>
        <button type="submit">Update Configuration</button>
      </form>
    </div>
  );
};

export default ConfigForm;
