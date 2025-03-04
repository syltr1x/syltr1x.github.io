import {defineCollection, z} from "astro:content";

const themes = defineCollection({
	schema: z.object({
		title: z.string(),
		description: z.string(),
		img: z.string(),
		date: z.string(),
		tags: z.array(z.string()),
	})
})

const projects = defineCollection({
	schema: z.object({
		title: z.string(),
		description: z.string(),
		img: z.string(),
		client: z.string(),
		tags: z.array(z.string()),
		url: z.string().url(),
	})
})

export const collections = { themes, projects }
