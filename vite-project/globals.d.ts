// src/globals.d.ts
export interface Configs {
    sentryKey: string;
    environment: string;
    tracePropagationTargets: string[];
    sentryProjectId: string;
    // Add other properties as needed
}

declare global {
    interface Window {
        configs: Configs;
    }
}

// This makes the file a module and avoids the error TS2669
export {};
