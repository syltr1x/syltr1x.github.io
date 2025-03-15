import {defineCollection, z} from "astro:content";

const posts = defineCollection({
	schema: z.object({
		title: z.string(),
		description: z.string(),
		date: z.string(),
		tags: z.array(z.string()),
	})
})

const projects = defineCollection({
	schema: z.object({
		title: z.string(),
		description: z.string(),
		client: z.string(),
		tags: z.array(z.string()),
		url: z.string().url(),
		url_repo: z.string().url(),
	})
})

export const collections = { posts, projects }
